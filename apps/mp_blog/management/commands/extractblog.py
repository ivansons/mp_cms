from __future__ import absolute_import
from __future__ import unicode_literals

import json

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

import untangle


class NoDefaultProvided(object):
    pass


def _getattr(obj, name, default=NoDefaultProvided):
    try:
        return reduce(getattr, name.split("."), obj)
    except (AttributeError, IndexError) as e:
        if default != NoDefaultProvided:
            return default
        raise e


class Command(BaseCommand):
    help = 'Extract blog entries from XML file dumped from WordPress site. ' \
           'The results will be saved to json file.'
    entry_types = {'post'}

    def add_arguments(self, parser):
        parser.add_argument(
            'xml_file', nargs='?',
            help='XML file dumped from WordPress site.'
        )

        parser.add_argument(
            '-o', '--output', dest='output',
            help='filename of output file'
        )

    def handle(self, *args, **options):
        """
        Extract blog entries from a given XML file
        """
        if not options['xml_file']:
            raise CommandError('Please provide a XML file')

        if not options['output']:
            raise CommandError('Please provide a output filename')

        xml_obj = untangle.parse(options['xml_file'])

        entries = self.get_entries(xml_obj)

        with open(options['output'], 'w') as f:
            json.dump(entries, f)

    def get_attachments(self, xml_obj):
        channel = xml_obj.rss.channel
        attachments = {}
        for i in channel.item:
            if i.wp_post_type.cdata != 'attachment':
                continue
            attachments[i.wp_post_id.cdata] = i.wp_attachment_url.cdata
        return attachments

    def get_entries(self, xml_obj):
        attachments = self.get_attachments(xml_obj)
        channel = xml_obj.rss.channel
        entries = []
        for i in channel.item:
            if i.wp_post_type.cdata not in self.entry_types:
                continue
            title = i.title.cdata.strip()
            categories = _getattr(i, 'category', [])
            if type(categories) != list:
                categories = [categories]
            postmeta = _getattr(i, 'wp_postmeta', [])
            if type(postmeta) != list:
                postmeta = [postmeta]
            meta = {
                x.wp_meta_key.cdata: x.wp_meta_value.cdata for x in postmeta
            }
            if '_thumbnail_id' in meta:
                thumbnail = attachments[meta['_thumbnail_id']]
            else:
                thumbnail = None
            entry = {
                'post_type': i.wp_post_type.cdata,
                'slug': i.wp_post_name.cdata or slugify(title),
                'title': title,
                'post_status': i.wp_status.cdata,
                'categories': ', '.join([
                    c.cdata for c in categories if c['domain'] == 'category']),
                'tags': ', '.join([
                    c.cdata for c in categories if c['domain'] == 'post_tag']),
                'link': i.link.cdata,
                'content': i.content_encoded.cdata,
                'creator': i.dc_creator.cdata,
                'date': i.wp_post_date.cdata,
                'date_gmt': i.wp_post_date_gmt.cdata,
                'date_pub': i.pubDate.cdata,
                'thumbnail': thumbnail,
                'meta': meta
            }
            entries.append(entry)
        return entries
