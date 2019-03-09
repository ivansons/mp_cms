# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='display_author',
            field=models.CharField(max_length=255, verbose_name='Display author', blank=True),
        ),
    ]
