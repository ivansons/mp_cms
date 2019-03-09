# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0021_add_matterapps'),
    ]

    operations = [
        migrations.AddField(
            model_name='matterappsentry',
            name='price_option',
            field=models.BooleanField(default=False, verbose_name='Starting at'),
        ),
        migrations.AlterField(
            model_name='matterappsentry',
            name='company_description',
            field=models.TextField(null=True, verbose_name='company description', blank=True),
        ),
        migrations.AlterField(
            model_name='matterappsentry',
            name='company_name',
            field=models.CharField(max_length=150, null=True, verbose_name='company', blank=True),
        ),
        migrations.AlterField(
            model_name='matterappsentry',
            name='company_url',
            field=models.URLField(help_text='Link to company.', max_length=150, null=True, verbose_name='company link', blank=True),
        ),
        migrations.AlterField(
            model_name='matterappsentry',
            name='compatibility',
            field=models.CharField(default='Nothing', max_length=150, verbose_name='compatibility', blank=True),
        ),
    ]
