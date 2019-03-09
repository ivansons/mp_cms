# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_builder', '0002_add_site_to_callout'),
        ('mp_widgets', '0026_rawpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoHeaderFooterLayout',
            fields=[
                ('maincontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='page_builder.MainContent')),
            ],
            options={
                'verbose_name': 'no header and footer',
                'verbose_name_plural': 'no header and footer',
            },
            bases=('page_builder.maincontent',),
        ),
        migrations.CreateModel(
            name='WordPressLayout',
            fields=[
                ('maincontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='page_builder.MainContent')),
            ],
            options={
                'verbose_name': 'word press page',
                'verbose_name_plural': 'word press pages',
            },
            bases=('page_builder.maincontent',),
        ),
        migrations.AlterField(
            model_name='rawpage',
            name='response_content_type',
            field=models.CharField(default=b'text/html', max_length=255, verbose_name='Response content type', choices=[(b'text/html', 'HTML'), (b'text/plain', 'Plain text'), (b'application/json', 'JSON'), (b'application/xml', 'XML')]),
        ),
    ]
