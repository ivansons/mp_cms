# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0019_review_queue_initialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabpanel',
            name='hashtag',
            field=models.CharField(default=b'', help_text='Each tab panel nees a unique hashtag', max_length=32, verbose_name='Hashtag', blank=True),
        ),
    ]
