# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields
import widgy.contrib.page_builder.db.fields
import django.db.models.deletion
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0010_featuresectionvideo_iframe_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', colorful.fields.RGBColorField(default=b'', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', colorful.fields.RGBColorField(default=b'', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', colorful.fields.RGBColorField(default=b'', blank=True)),
                ('main_title_size', models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('main_title_is_raw_html', models.BooleanField(default=False, verbose_name='Is main title raw HTML?')),
                ('text_align', models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')])),
                ('background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Section Container',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.AddField(
            model_name='sixup',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='sixup',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='sixup',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='stats',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='stats',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='stats',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='main_title_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main title raw HTML?'),
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h7)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='text_align',
            field=models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')]),
        ),
    ]
