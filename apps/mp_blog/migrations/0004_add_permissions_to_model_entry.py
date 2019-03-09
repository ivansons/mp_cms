# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0003_rename_model_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelentry',
            options={'ordering': ['-creation_date'], 'get_latest_by': 'creation_date', 'verbose_name': 'model entry', 'verbose_name_plural': 'model entries', 'permissions': (('can_view_all_models', 'Can view all entries'), ('can_change_model_status', 'Can change status'), ('can_change_model_author', 'Can change author(s)'))},
        ),
        migrations.AlterIndexTogether(
            name='modelentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication')]),
        ),
    ]
