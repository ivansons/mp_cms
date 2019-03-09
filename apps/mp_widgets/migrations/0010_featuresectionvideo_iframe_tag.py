# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.mp_widgets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0009_featuresection_large_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuresectionvideo',
            name='video',
        ),
        migrations.AddField(
            model_name='featuresectionvideo',
            name='iframe_tag',
            field=apps.mp_widgets.fields.IframeTagField(default=b'<iframe></iframe>', max_length=1000, verbose_name='iFrame Tag', blank=True),
        ),
    ]
