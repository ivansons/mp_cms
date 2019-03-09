# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0012_modelentry_refresh_model_info'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelentry',
            options={'ordering': ['-featured', '-sort_order', '-creation_date'], 'get_latest_by': 'creation_date', 'verbose_name': 'model entry', 'verbose_name_plural': 'model entries', 'permissions': (('can_view_all_models', 'Can view all entries'), ('can_change_model_status', 'Can change status'), ('can_change_model_author', 'Can change author(s)'))},
        ),
        migrations.AlterField(
            model_name='modelentry',
            name='refresh_model_info',
            field=models.BooleanField(default=False, help_text='Reload model info from API', verbose_name='Refresh model info'),
        ),
        migrations.AlterField(
            model_name='modelentry',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (2, 'published')]),
        ),
    ]
