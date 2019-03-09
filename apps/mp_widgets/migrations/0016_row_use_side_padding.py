# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0015_column_width_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='row',
            name='use_side_padding',
            field=models.BooleanField(default=True, verbose_name='Padding both sides'),
        ),
    ]
