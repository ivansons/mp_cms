# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0030_improve_wp_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordpresslayout',
            name='custom_scripts',
            field=models.TextField(default=b'', help_text='One file per line', verbose_name='Custom JavaScript', blank=True),
        ),
    ]
