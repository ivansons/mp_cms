# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0029_realestateverticallayout'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordpresslayout',
            name='body_css_class',
            field=models.CharField(default=b'', max_length=255, verbose_name='Body CSS class', blank=True),
        ),
        migrations.AddField(
            model_name='wordpresslayout',
            name='custom_stylesheets',
            field=models.TextField(default=b'', help_text='One file per line', verbose_name='Custom stylesheets', blank=True),
        ),
    ]
