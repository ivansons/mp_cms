# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import widgy.contrib.page_builder.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0011_section_baseup_improvement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabPanel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, verbose_name='Title', blank=True)),
                ('hashtag', models.CharField(default=b'', max_length=32, verbose_name='Hashtag', blank=True)),
                ('icon', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Icon image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'Tab Panel',
            },
        ),
        migrations.CreateModel(
            name='TabPanelContainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Tab Panel Container',
            },
        ),
        migrations.AlterField(
            model_name='section',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='sixup',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='stats',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='threeupicon',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='threeupimage',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='threeuplongtext',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='threeupoverlay',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
        migrations.AlterField(
            model_name='twoupoverlay',
            name='main_title_size',
            field=models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]
