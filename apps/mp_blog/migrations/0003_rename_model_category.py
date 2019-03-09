# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0002_newscategory_newsentry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelcategory',
            options={'ordering': ['title'], 'verbose_name': 'model category', 'verbose_name_plural': 'model categories'},
        ),
    ]
