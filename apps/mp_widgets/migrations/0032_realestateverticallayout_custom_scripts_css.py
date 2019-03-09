# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0031_wordpresslayout_custom_scripts'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestateverticallayout',
            name='custom_scripts',
            field=models.TextField(help_text='One file per line', verbose_name='Custom JavaScript', blank=True),
        ),
        migrations.AddField(
            model_name='realestateverticallayout',
            name='custom_stylesheets',
            field=models.TextField(help_text='One file per line', verbose_name='Custom stylesheets', blank=True),
        ),
    ]
