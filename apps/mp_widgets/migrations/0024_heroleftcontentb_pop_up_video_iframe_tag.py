# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.mp_widgets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0023_downloadfile_download_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroleftcontentb',
            name='pop_up_video_iframe_tag',
            field=apps.mp_widgets.fields.IframeTagField(default=b'<iframe></iframe>', max_length=1000, verbose_name='Pop-up Video iFrame Tag', blank=True),
        ),
    ]
