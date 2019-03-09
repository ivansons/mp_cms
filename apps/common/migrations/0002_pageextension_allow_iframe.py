# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageextension',
            name='allow_iframe',
            field=models.NullBooleanField(help_text='Unknown: system default<br />Yes: allow iframe requests (no "X-Frame-Options" header)<br />No: deny iframe requests (set "X-Frame-Options" to "DENY")', verbose_name='Allow iframe embedding'),
        ),
    ]
