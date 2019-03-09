# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0019_regionentry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='regionentry',
            name='in_footer',
            field=models.BooleanField(default=False),
        ),
    ]
