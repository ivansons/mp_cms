# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import apps.mp_widgets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0020_help_text_for_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabpanel',
            name='icon',
            field=apps.mp_widgets.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Icon image', blank=True, to='filer.File', null=True),
        ),
    ]
