# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0008_colorful'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuresection',
            name='large_image',
            field=models.BooleanField(default=False),
        ),
    ]
