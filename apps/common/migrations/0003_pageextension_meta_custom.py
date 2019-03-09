# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_pageextension_allow_iframe'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageextension',
            name='meta_custom',
            field=models.TextField(help_text='Raw HTML', verbose_name='Custom HTML content in head (extra)', blank=True),
        ),
    ]
