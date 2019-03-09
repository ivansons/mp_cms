# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0025_auto_20171128_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudyentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
        migrations.AddField(
            model_name='matterappsentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
        migrations.AddField(
            model_name='modelentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
        migrations.AddField(
            model_name='newsentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
        migrations.AddField(
            model_name='regionentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
        migrations.AddField(
            model_name='resourceentry',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
    ]
