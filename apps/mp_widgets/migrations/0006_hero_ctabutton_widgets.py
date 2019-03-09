# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.contrib.page_builder.db.fields
import django.db.models.deletion
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('mp_widgets', '0005_singlecta_threeupimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, verbose_name='text', blank=True)),
                ('link_object_id', models.PositiveIntegerField(null=True, editable=False)),
                ('link_content_type', models.ForeignKey(related_name='+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name': 'CTA Button',
            },
            bases=(widgy.models.mixins.StrDisplayNameMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bg_video_url', models.CharField(default=b'video url', max_length=255, verbose_name='background video url', blank=True)),
                ('bg_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='maps', on_delete=django.db.models.deletion.PROTECT, verbose_name='background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HeroLeftContentA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Hero Left Content A',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HeroLeftContentB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Hero Left Content B',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='HeroRightContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Hero RightContent',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RightContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, verbose_name='Title', blank=True)),
                ('text', models.CharField(default=b'Text', max_length=255, verbose_name='Text', blank=True)),
            ],
            options={
                'verbose_name': 'RightContent Carousel',
            },
        ),
    ]
