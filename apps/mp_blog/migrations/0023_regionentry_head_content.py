# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0022_update_matterapps'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionentry',
            name='head_content',
            field=models.TextField(help_text='Add content to <head></head> when page is rendered', null=True, verbose_name='head content', blank=True),
        ),
    ]
