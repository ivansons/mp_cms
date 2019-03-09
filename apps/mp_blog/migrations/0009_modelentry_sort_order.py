# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0008_modelentry_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelentry',
            name='sort_order',
            field=models.IntegerField(default=0, db_index=True, blank=True),
            preserve_default=False,
        ),
        migrations.AlterModelOptions(
            name='modelentry',
            options={'ordering': ['-featured', 'sort_order', '-creation_date'], 'get_latest_by': 'creation_date', 'verbose_name': 'model entry', 'verbose_name_plural': 'model entries', 'permissions': (('can_view_all_models', 'Can view all entries'), ('can_change_model_status', 'Can change status'), ('can_change_model_author', 'Can change author(s)'))},
        ),
    ]
