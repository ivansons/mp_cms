# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import widgy.contrib.page_builder.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, blank=True)),
                ('text_is_raw_html', models.BooleanField(default=False)),
                ('text', models.TextField(default=b'Text', blank=True)),
                ('hyperlink1_text', models.CharField(default=b'Hyperlink Text 1', max_length=255, verbose_name='Hyperlink #1 Text', blank=True)),
                ('hyperlink1_url', models.CharField(default=b'Hyperlink URL 1', max_length=255, verbose_name='Hyperlink #1 URL', blank=True)),
                ('hyperlink2_text', models.CharField(default=b'Hyperlink Text 2', max_length=255, verbose_name='Hyperlink #2 Text', blank=True)),
                ('hyperlink2_url', models.CharField(default=b'Hyperlink URL 2', max_length=255, verbose_name='Hyperlink #2 URL', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.CharField(default=b'', max_length=1000, verbose_name='CSS style', blank=True)),
                ('content_is_on_left', models.BooleanField(default=True)),
                ('background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='background image', blank=True, to='filer.File', null=True)),
                ('foreground_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='foreground image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'feature section',
            },
        ),
    ]
