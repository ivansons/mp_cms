from __future__ import absolute_import
from __future__ import unicode_literals

from django.core.management.base import BaseCommand, CommandError

from zinnia.managers import PUBLISHED

from apps.mp_blog.models import ModelEntry

GALLERY_LINK_ATTRIBUTES = ['model_link', 'model_vr_link', 'creator_link',
                           'presenter_link']


class Command(BaseCommand):
    help = 'Find all URLs and links associated with Gallery model entries'

    def add_arguments(self, parser):
        parser.add_argument('gallery_urls_output_file', nargs='?',
                            help='output file containing the gallery urls')

    def handle(self, *args, **options):
        """
        Write a list of Gallery URLs to an output file

        """
        if not options['gallery_urls_output_file']:
            raise CommandError('Please provide an output file to write urls '
                               'to')

        self.find_gallery_urls(options['gallery_urls_output_file'])

    def find_gallery_urls(self, output_file):
        """
        Find gallery urls and associated links

        :param output_file: Filename
        :return: None

        """
        gallery_models = ModelEntry.objects.filter(status=PUBLISHED)

        with open(output_file, 'w') as target_file:

            # Loop over Gallery model entries
            for g_model in gallery_models:
                urls_for_one_model = set()

                url = 'https://matterport.com{}'.format(
                    g_model.get_absolute_url())

                url2 = 'https://matterport.com/blog{}'.format(
                    g_model.get_absolute_url())

                # Add the url
                urls_for_one_model.add(url)
                urls_for_one_model.add(url2)

                # Add in related model entry links or default '' if exception
                # raised
                for attribute in GALLERY_LINK_ATTRIBUTES:
                    urls_for_one_model.add(getattr(g_model, attribute, ''))


                urls_for_one_model.discard('')

                # Write to the output file if there is at least one URL
                if urls_for_one_model:
                    if g_model.title:

                        # Remove non ascii characters
                        title = g_model.title.encode('ascii', 'ignore')
                        target_file.write('# -- {}\n'.format(title))
                    else:
                        target_file.write('# -- {}\n'.format(url))

                    for url in urls_for_one_model:
                        target_file.write('{}\n'.format(url))
