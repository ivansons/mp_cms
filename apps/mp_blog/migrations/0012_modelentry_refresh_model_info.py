# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0011_modelentry_add_creator_n_presenter'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelentry',
            name='refresh_model_info',
            field=models.BooleanField(default=False, help_text='Display Model Embed Code', verbose_name='Refresh model info'),
        ),
    ]
