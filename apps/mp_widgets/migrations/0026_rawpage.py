# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.db.fields
import django.db.models.deletion
import widgy.contrib.widgy_mezzanine.models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('review_queue', '0001_initial'),
        ('mp_widgets', '0025_baseup_main_text_is_raw_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('response_content_type', models.CharField(default=b'text/plain', max_length=255, verbose_name='Response content type', choices=[(b'text/html', 'HTML'), (b'text/plain', 'Plain text'), (b'application/json', 'JSON'), (b'application/xml', 'XML')])),
                ('root_node', widgy.db.fields.VersionedWidgyField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='widgy content', to='review_queue.ReviewedVersionTracker', null=True)),
            ],
            options={
                'ordering': ('_order',),
                'swappable': 'WIDGY_MEZZANINE_PAGE_MODEL',
                'verbose_name': 'raw page',
                'verbose_name_plural': 'raw pages',
            },
            bases=(widgy.contrib.widgy_mezzanine.models.WidgyPageMixin, 'pages.page'),
        ),
    ]
