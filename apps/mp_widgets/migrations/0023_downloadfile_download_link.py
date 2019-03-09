# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0022_downloadfile_mspmaterial'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadfile',
            name='download_link',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
