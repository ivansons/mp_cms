from __future__ import absolute_import
from __future__ import unicode_literals

import json
import logging
import re

from django.core.management.base import BaseCommand, CommandError

from pyquery import PyQuery
import requests

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Crawl all models from live WP site, extract information and ' \
           'save to json file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--output', dest='output',
            help='filename of output file'
        )

    def handle(self, *args, **options):
        """
        Parse gallery page to get a list of urls and crawl all the information
        """
        if not options['output']:
            raise CommandError('Please provide a output filename')

        entries = []
        urls = self.get_urls()

        for url in reversed(urls):
            entries.append(self.crawl_url(url))
            logger.info('crawl space - %s', url)

        with open(options['output'], 'w') as f:
            json.dump(entries, f)

    def get_urls(self):
        """
        Parse urls from gallery page of live site

        :return: A list of urls
        """
        resp = requests.get('')
        d = PyQuery(resp.content)

        urls = []
        for a in d('.spaces-item > a'):
            urls.append(a.attrib['href'])

        return urls

    def crawl_url(self, url):
        """
        Crawl model page and extract information from url

        :param url: Url in string to crawl
        :return: A dictionary representation of model
        """
        slug = re.search('(?<=/3d-space/).*', url).group(0)
        slug = slug.strip('/')

        resp = requests.get(url)
        d = PyQuery(resp.content)

        creator_url = None
        presenter_url = None

        for a in d('#model-contact-wrap a'):
            if 'presented-span' in PyQuery(a).__html__():
                presenter_url = a.attrib['href']
            else:
                creator_url = a.attrib['href']

        return {
            'slug': slug,
            'title': d('.presented-by h1').text(),
            'category': d('h3.more-related a').text(),
            'creator_url': creator_url,
            'presenter_url': presenter_url,
            'model_link': d('.wp3d-embed-wrap iframe').attr('src'),
            'model_vr_link': d('#model-vr-link').attr('href'),
            'content': d('div.model-summary').__html__(),
            'post_type': 'model',
            'post_status': 'publish',
            'keywords': d('meta[name=keywords]').attr('content'),
        }
