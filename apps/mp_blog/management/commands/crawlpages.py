from __future__ import absolute_import
from __future__ import unicode_literals

import json

from django.core.management.base import BaseCommand, CommandError

from pyquery import PyQuery
import requests


class Command(BaseCommand):
    help = 'Crawl all pages from live WP site, extract information and ' \
           'save to json file'

    def add_arguments(self, parser):
        parser.add_argument(
            'urls_file', nargs='?',
            help='file containing all the urls to crawl.'
        )

        parser.add_argument(
            '-o', '--output', dest='output',
            help='filename of output file'
        )

    def handle(self, *args, **options):
        """
        Read a list of urls from given file and crawl all the information
        """
        if not options['urls_file']:
            raise CommandError('Please provide a file of page urls')

        if not options['output']:
            raise CommandError('Please provide a output filename')

        pages = []

        urls = self.load_urls(options['urls_file'])
        for url in urls:
            pages.append(self.crawl_url(url))

        with open(options['output'], 'w') as f:
            json.dump(pages, f)

    def load_urls(self, urls_file):
        """
        Load urls from given file

        :param urls_file: Filename
        :return: A list of urls
        """
        with open(urls_file) as f:
            content = f.read().strip()
            urls = [l.strip() for l in content.split() if l.strip()]
        return urls

    def crawl_url(self, url):
        """
        Crawl page and extract information from url

        :param url: Url in string to crawl
        :return: A dictionary representation of page
        """
        hostname = ''
        resp = requests.get('https://{}{}'.format(hostname, url))
        d = PyQuery(resp.content)

        body_cls = d('body').attr('class')
        if body_cls:
            d('#content-height').attr('class', body_cls)

        return {
            'slug': url,
            'title': d('head>title').text(),
            'description': d('meta[name=description]').attr('content'),
            'keywords': d('meta[name=keywords]').attr('content'),
            'content': d('#content-height').__html__(),
            'post_type': 'static_page',
            'post_status': 'publish',
        }
