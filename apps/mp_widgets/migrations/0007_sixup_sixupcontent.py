# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.contrib.page_builder.db.fields
import django.db.models.deletion
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0006_hero_ctabutton_widgets'),
    ]

    operations = [
        migrations.CreateModel(
            name='SixUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
            ],
            options={
                'verbose_name': '6-Up',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SixUpContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, verbose_name='Title', blank=True)),
                ('url_text', models.CharField(default=b'url Text', max_length=255, verbose_name='url Text', blank=True)),
                ('url', models.CharField(default=b'url', max_length=255, verbose_name='url', blank=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': '6-Up Content',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
    ]
