# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0007_modelentry__model_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelentry',
            name='tags',
            field=tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True),
        ),
    ]
