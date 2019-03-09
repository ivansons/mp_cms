from __future__ import absolute_import
from __future__ import unicode_literals

from cStringIO import StringIO
import json
import logging
import re

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError
from django.utils.dateparse import parse_datetime
from django.utils.html import escape
from django.utils.text import normalize_newlines, slugify

from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from mezzanine.generic.models import AssignedKeyword, Keyword

from pyquery import PyQuery
import pytz
import requests

from widgy.contrib.page_builder.models import UnsafeHtml

from zinnia.managers import DRAFT, PUBLISHED
from zinnia.models import Category, Entry

from project.widgy_site import site
from apps.mp_blog.models import (ModelCategory, ModelEntry,
                                 NewsCategory, NewsEntry)
from apps.mp_widgets.models import (WordPressLayout, NoHeaderFooterLayout,
                                    RealEstateVerticalLayout, RawPage)
from ...utils import upload_image_to_s3

REAL_ESTATE_VERTICAL_SLUGS = [
    'real-estate-customer-testimonials', '3d-virtual-tour-pricing',
    'easy-3d-scanning-update-your-listing', 'easy-3d-scanning-win-the-listing',
    'easy-3d-tours-scan-the-home', 'why-use-3d-real-estate-agents',
    '3d-for-real-estate-brokerages', 'real-estate-why-use-3d-photographers',
    'real-estatewhy-use-3d-photographers', '3d-marketing-for-real-estate'
]

User = get_user_model()
logger = logging.getLogger(__name__)


def linebreaks(value, autoescape=False):
    """
    Override django's built-in linebreaks
    to avoid putting h1 ~ h6, ol, and ul inside p
    """
    def _legal_in_p(c):
        illegal_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li']
        return not any(['<{}>'.format(x) in c for x in illegal_tags])

    def _wrap(c):
        if autoescape:
            c = escape(c)
        c = c.replace('\n', '<br />')
        if _legal_in_p(c):
            c = '<p>%s</p>' % c
        return c

    value = normalize_newlines(value)
    paras = re.split('\n{2,}', value)
    paras = [_wrap(p) for p in paras]

    return '\n\n'.join(paras)


class Command(BaseCommand):
    help = 'Load content from a dump file of live WP site in json format'

    def add_arguments(self, parser):
        parser.add_argument(
            'wp_file', nargs='?',
            help='file dumped from live WP site in json format'
        )
        parser.add_argument(
            '--blog', action='store_true',
            help='import blog contents'
        )
        parser.add_argument(
            '--news', action='store_true',
            help='import news contents'
        )
        parser.add_argument(
            '--model', action='store_true',
            help='import gallery model contents'
        )
        parser.add_argument(
            '--page', action='store_true',
            help='import pages'
        )

    def handle(self, *args, **options):
        if not options['wp_file']:
            raise CommandError('Please provide a file to load')

        content_types = set({})
        if options['blog']:
            content_types.add('post')
        if options['news']:
            content_types.add('news_type')
        if options['model']:
            content_types.add('model')
        if options['page']:
            content_types.add('static_page')
        if not content_types:
            content_types = {'post', 'news_type', 'model', 'static_page'}

        self.content_types = content_types
        self.loaddata(options['wp_file'])

    def loaddata(self, wp_file):
        """
        Read entries from file and import to database

        :param wp_file: filename of dumped content in json format
        """
        with open(wp_file) as f:
            data = json.load(f, encoding='latin-1')

            for item in data:
                if item['post_type'] in self.content_types \
                        and item['post_status'] == 'publish':
                    func = self.get_handling_func(item['post_type'])
                    func(item)

    def get_handling_func(self, content_type):
        """
        Different handling functions are defined to import contents of
        different types.

        :param content_type: content type of entry
        :return: handling function
        """
        if content_type == 'post':
            func = self.load_blog
        elif content_type == 'news_type':
            func = self.load_news
        elif content_type == 'model':
            func = self.load_model
        elif content_type == 'static_page':
            func = self.load_page
        else:
            raise CommandError("Unrecognized content type '%s'. Aborting."
                               % content_type)
        return func

    def load_blog(self, item):
        """
        Import content as blog entry

        :param item: entry in json format
        """
        slug = item['slug']

        if Entry.objects.filter(slug=slug).exists():
            return

        status_dict = {
            'draft': DRAFT,
            'publish': PUBLISHED,
        }

        content = self.linebreaks(
            self.process_images(item['content']))

        entry = Entry(
            title=item['title'],
            slug=slug,
            status=status_dict[item['post_status']],
            creation_date=self.localtime(item['date']),
            content=content,
        )

        if item['meta'].get('author'):
            entry.display_author = item['meta']['author'].split(',')[0]

        if item['tags'] and item['tags'].strip():
            entry.tags = item['tags']

        if item['thumbnail']:
            resp = requests.get(item['thumbnail'])
            entry.image.save(item['thumbnail'].split('/')[-1],
                             ImageFile(StringIO(resp.content)), save=False)

        entry.save()

        entry.sites.add(Site.objects.get_current())

        for category_title in item['categories'].split(', '):
            if category_title and category_title.strip():
                category_slug = slugify(category_title)
                category, _ = Category.objects.get_or_create(
                    slug=category_slug,
                    defaults={'title': category_title})
                entry.categories.add(category)

    def load_news(self, item):
        """
        Import content as news entry

        :param item: entry in json format
        """
        slug = item['slug']

        if NewsEntry.objects.filter(slug=slug).exists():
            return

        status_dict = {
            'draft': DRAFT,
            'publish': PUBLISHED,
        }

        content = self.linebreaks(
            self.process_images(item['content']))

        entry = NewsEntry(
            title=item['title'],
            slug=slug,
            status=status_dict[item['post_status']],
            creation_date=self.localtime(item['date']),
            content=content,
        )

        if item['news_icon']:
            entry.icon = upload_image_to_s3(item['news_icon'])

        if item['meta'].get('news_video_link'):
            entry.video_link = item['meta']['news_video_link']

        if item['meta'].get('external_link'):
            entry.external_link = item['meta']['external_link']

        if item['meta'].get('news_author'):
            entry.external_author = item['meta']['news_author']

        if item['meta'].get('news_author_url'):
            entry.external_author_url = item['meta']['news_author_url']

        entry.save()

        entry.sites.add(Site.objects.get_current())

        for category_title in item['categories'].split(', '):
            if category_title and category_title.strip():
                category_slug = slugify(category_title)
                category, _ = NewsCategory.objects.get_or_create(
                    slug=category_slug,
                    defaults={'title': category_title})
                entry.categories.add(category)

    def load_model(self, item):
        """
        Import content as gallery model entry

        :param item: entry in json format
        """
        if ModelEntry.objects.filter(slug=item['slug']).exists():
            return
        entry = ModelEntry(
            slug=item['slug'],
            status=PUBLISHED,
            model_link=item['model_link'],
            model_vr_link=item['model_vr_link'] or '',
        )
        try:
            entry.save()
        except Exception:
            return
        entry.sites.add(Site.objects.get_current())

        if item['category'] and item['category'].strip():
            category_slug = slugify(item['category'])
            category, _ = ModelCategory.objects.get_or_create(
                slug=category_slug,
                defaults={'title': item['category']})
            entry.categories.add(category)
        if item['title']:
            entry.title = item['title']
        if item['creator_url'] and item['creator_url'].startswith('http'):
            entry.creator_link = item['creator_url'].strip()
        if item['presenter_url'] and item['presenter_url'].startswith('http'):
            entry.presenter_link = item['presenter_url'].strip()
        if item['content']:
            entry.content = self.process_images(item['content'])
            
        entry.save()

        logger.info('load space - %s', item['model_link'])

    def load_page(self, item):
        """
        Import content as mezzanine page

        :param item: entry in json format
        """
        # create widgy page
        page = RawPage(
            title=item['title'],
            gen_description=False if item['description'] else True,
            description=item['description'] or '',
            _meta_title=item['title'],
            slug=item['slug'].strip('/') or '/',
            status=CONTENT_STATUS_PUBLISHED,
            site=Site.objects.get_current()
        )
        if page.slug in REAL_ESTATE_VERTICAL_SLUGS:
            content_type = \
                ContentType.objects.get_for_model(RealEstateVerticalLayout)
        elif page.slug in {
            'terms-of-use',
            'legal/eula',
            'legal/camera-terms-of-sale',
            'legal/terms-of-service'
        }:
            content_type = ContentType.objects.get_for_model(NoHeaderFooterLayout)
        else:
            content_type = ContentType.objects.get_for_model(WordPressLayout)
        setattr(page, 'root_node', content_type)
        page.save()

        # add keywords
        keywords = []
        if item['keywords']:
            keywords = [keyword.strip()
                        for keyword in item['keywords'].split(',')]
        for keyword in set(keywords):
            keyword_obj, _ = Keyword.objects.get_or_create(title=keyword)
            page.keywords.add(AssignedKeyword(keyword=keyword_obj))

        # create content
        page.root_node.working_copy.content.add_child(
            site,
            UnsafeHtml,
            content=self.process_images(item['content'])
        )
        page = RawPage.objects.get(id=page.id)
        commit = page.root_node.commit()

        # approve and publish
        user, _ = User.objects.get_or_create(username='WP_Loader',
                                             is_superuser=True)
        commit.approve(user)

    def localtime(self, date_str):
        """
        Generate datetime object with timezone from date string

        :param date_str: date string
        """
        t = parse_datetime(date_str)
        return pytz.timezone('US/Pacific').localize(t)

    def process_images(self, content):
        """
        Upload images in the given content to Amazon S3, and replace image url
        in the content.

        :param content: HTML content that has image
        """
        d = PyQuery(content)

        images_to_upload = []

        for img in d('img'):
            link = img.attrib.get('src', '')
            link_strip = link.strip()
            if link_strip and link_strip.startswith('http'):
                images_to_upload.append(link)

        for element in d('[style*="background-image:"]'):
            match = re.search('https.*?(?=\'?\))',
                              PyQuery(element).attr.style)
            if match:
                images_to_upload.append(match.group(0))

        for link in set(images_to_upload):
            try:
                image = upload_image_to_s3(link.strip())
            except IOError:
                continue
            content = re.sub(link, image.url, content)

        return content

    def linebreaks(self, content):
        """Converts newlines into <p> and <br />s."""
        # Separate h1 ~ h6, ul, and ol so they won't go into <p> tag
        for e in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol']:
            opening_tag = '<{}>'.format(e)
            closing_tag = '</{}>'.format(e)
            content = content.replace(opening_tag,
                                      '\n\n{}'.format(opening_tag))
            content = content.replace(closing_tag,
                                      '{}\n\n'.format(closing_tag))
        # Remove <br /> after ol, ul, and li
        d = PyQuery(linebreaks(content))
        for e in ['ol+br', 'ol>br', 'ul+br', 'ul>br', 'li+br']:
            d(e).remove()
        # Remove height attribute of image
        for e in d('img'):
            if 'height' in e.attrib:
                del e.attrib['height']
        # Remove `content` class that breaks entries' styling
        d('div.content').removeClass('content')
        return d.__html__()
