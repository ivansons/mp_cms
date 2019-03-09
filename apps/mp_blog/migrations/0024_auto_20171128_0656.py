# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0023_regionentry_head_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionentry',
            name='head_content',
            field=models.TextField(help_text='Add content to "<head></head>" when page is rendered', null=True, verbose_name='head content', blank=True),
        ),
    ]
