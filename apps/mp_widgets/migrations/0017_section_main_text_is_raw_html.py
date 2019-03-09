# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0016_row_use_side_padding'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='main_text_is_raw_html',
            field=models.BooleanField(default=False, verbose_name='Is main text raw HTML?'),
        ),
    ]
