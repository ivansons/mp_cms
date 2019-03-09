from __future__ import absolute_import
from __future__ import unicode_literals

import csv

from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Creates redirects from input csv file.  The first column is the ' \
           'old url and the second column is the url to redirect to.'

    def add_arguments(self, parser):
        parser.add_argument('redirects_file', nargs='?',
                            help='file containg the redirects to create')

    def handle(self, *args, **options):
        """
        Read a list of redirects from given file and create django redirects

        The provided file should be a csv with first column being the original
        url and the second column being the url to redirect to.

        """
        if not options['redirects_file']:
            raise CommandError('Please provide a file of redirects')

        self.load_redirects(options['redirects_file'])

    def load_redirects(self, redirects_file):
        """
        Load redirect urls from given file and creates django redirects

        :param redirects_file: Filename
        :return: None

        """
        site = Site.objects.get_current()

        with open(redirects_file, 'rb') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                try:
                    self.create_redirect(site=site, start=row[0], end=row[1])

                except:
                    print('ERROR: Row could not be converted: {}'.format(row))

    def create_redirect(self, site, start, end):
        """
        Create / modify a django redirect

        :param site: Site
        :param start: str
        :param end: str

        return: None

        """
        redirect, created = Redirect.objects.get_or_create(site=site,
                                                           old_path=start)

        redirect.new_path = end
        redirect.save()

        log_str = ' with starting url: {}'.format(start)
        if created:
            log_str = 'Created new redirect' + log_str
        else:
            log_str = 'Modified existing redirect' + log_str

        print(log_str)
