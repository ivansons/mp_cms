# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.file
import widgy.models.mixins
import django.db.models.deletion
import apps.mp_widgets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0021_icon_field_acceptted_more_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('download_file', filer.fields.file.FilerFileField(blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Download File',
            },
        ),
        migrations.CreateModel(
            name='MspMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('main_title_size', models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('main_title_is_raw_html', models.BooleanField(default=False, verbose_name='Is main title raw HTML?')),
                ('text_align', models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')])),
                ('upper_left_text', models.CharField(max_length=255, verbose_name='Upper left text', blank=True)),
                ('iframe_tag', apps.mp_widgets.fields.IframeTagField(default=b'<iframe></iframe>', max_length=1000, verbose_name='iFrame Tag', blank=True)),
                ('image', apps.mp_widgets.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Right image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'MSP Material',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
    ]
