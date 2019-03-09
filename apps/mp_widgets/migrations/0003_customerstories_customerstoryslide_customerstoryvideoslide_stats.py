# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.contrib.page_builder.db.fields
import django.db.models.deletion
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0002_auto_20160122_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerStories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
            ],
            options={
                'verbose_name': 'customer stories',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CustomerStorySlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_quote', models.CharField(default=b'Customer quote', max_length=255, verbose_name='Customer quote', blank=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'customer story slide',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CustomerStoryVideoSlide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer_quote', models.CharField(default=b'Customer quote', max_length=255, verbose_name='Customer quote', blank=True)),
                ('video', widgy.contrib.page_builder.db.fields.VideoField(help_text='Please enter a link to the YouTube or Vimeo page for this video.  i.e. http://www.youtube.com/watch?v=9bZkp7q19f0', null=True, verbose_name='Video', blank=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
                ('video_background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Video background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'customer story video slide',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
                ('background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'stats',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
    ]
