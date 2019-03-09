# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0027_rawpage_layouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='MspWebinarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_title', models.CharField(default=b'Webinar', max_length=255, verbose_name='Main title')),
                ('main_text', models.CharField(default=b'WEDNESDAY, AUG 10, 2016 | 11 AM PT | DURATION: 1H', max_length=255, verbose_name='Main text', blank=True)),
                ('sub_text', models.CharField(default=b'Topic Coming Soon', max_length=255, verbose_name='Secondary text', blank=True)),
                ('register_text', models.CharField(default=b'Register Now', max_length=255, verbose_name='Register Now text', blank=True)),
                ('register_link', models.URLField(verbose_name='Register Now link', blank=True)),
            ],
            options={
                'verbose_name': 'MSP Webinar Event',
            },
        ),
    ]
