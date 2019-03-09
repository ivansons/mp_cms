# -*- coding: utf-8 -*-
"""
ModelEntry `sort_order` initialization
"""
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # set `sort_order` value
    ModelEntry = apps.get_model('mp_blog', 'ModelEntry')

    for obj in ModelEntry.objects.all():
        obj.sort_order = obj.pk
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0009_modelentry_sort_order'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
    ]
