# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('mp_blog', '0018_add_region_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionentry',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Featured image.', null=True, verbose_name='Image'),
        ),
    ]
