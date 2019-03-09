# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0024_auto_20171128_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionentry',
            name='head_content',
            field=models.TextField(help_text='Add content to "head" when page is rendered', null=True, verbose_name='head content', blank=True),
        ),
    ]
