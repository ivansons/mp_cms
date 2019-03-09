# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_pageextension_meta_custom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageextension',
            options={'verbose_name': 'extension', 'verbose_name_plural': 'extensions'},
        ),
        migrations.AddField(
            model_name='pageextension',
            name='popup',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pageextension',
            name='subtitle',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
