# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0016_add_case_study'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='industrycategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='topiccategory',
            name='icon',
        ),
        migrations.RemoveField(
            model_name='typecategory',
            name='icon',
        ),
    ]
