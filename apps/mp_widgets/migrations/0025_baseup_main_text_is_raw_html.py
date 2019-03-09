# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0024_heroleftcontentb_pop_up_video_iframe_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='mspmaterial',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='sixup',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='stats',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='twoupembedcode',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
    ]
