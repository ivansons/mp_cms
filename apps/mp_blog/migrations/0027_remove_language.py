# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0026_auto_20171220_0542'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regionentry',
            options={'ordering': ('-featured', '-sort_order', '-creation_date'), 'get_latest_by': 'creation_date', 'verbose_name': 'region entry', 'verbose_name_plural': 'region entries', 'permissions': (('can_view_all_regions', 'Can view all entries'), ('can_change_region_status', 'Can change status'), ('can_change_region_author', 'Can change author(s)'))},
        ),
        migrations.AlterField(
            model_name='regionentry',
            name='slug',
            field=models.SlugField(unique=True, max_length=255, verbose_name='slug'),
        ),
        migrations.AlterIndexTogether(
            name='regionentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication')]),
        ),
        migrations.RemoveField(
            model_name='regionentry',
            name='language',
        ),
    ]
