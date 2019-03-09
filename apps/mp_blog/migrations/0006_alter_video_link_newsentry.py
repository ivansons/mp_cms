# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0005_categoryextension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsentry',
            name='video_link',
            field=models.URLField(help_text='How to get embedded links: <a href="https://support.google.com/youtube/answer/171780?hl=en" target="_blank">YouTube</a>, <a href="https://vimeo.com/help/faq/sharing-videos/embedding-videos#how-do-i-embed-a-video-on-another-site" target="_blank">Vimeo</a>. If you need assistance embedding a video from another website contact your site administrator.<br>Vimeo link example: https://player.vimeo.com/video/157326630', max_length=255, verbose_name='embed video link', blank=True),
        ),
    ]
