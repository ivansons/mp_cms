# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0006_alter_video_link_newsentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelentry',
            name='_model_info',
            field=models.TextField(verbose_name='Model Information', blank=True),
        ),
    ]
