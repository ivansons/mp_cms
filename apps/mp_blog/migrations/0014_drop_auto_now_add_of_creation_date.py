# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0013_modelentry_remove_hidden_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelentry',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True),
        ),
        migrations.AlterField(
            model_name='newsentry',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True),
        ),
    ]
