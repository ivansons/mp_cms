# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0035_update_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordpresslayout',
            name='og_tags',
            field=models.TextField(help_text='One file per line', verbose_name='Custom OG:Tags', blank=True),
        ),
    ]
