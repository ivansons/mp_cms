# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0014_hex_color_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='width',
            field=models.CharField(default=b'1/2', max_length=50, verbose_name='Column width', choices=[(b'1/3', '1/3 of row'), (b'1/2', '1/2 of row'), (b'2/3', '2/3 of row'), (b'3/3', '3/3 of row')]),
        ),
    ]
