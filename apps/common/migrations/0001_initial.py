# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_meta_robots', models.CharField(default=b'', help_text='Optional robots data to be used in the HTML meta data. If left blank, there will be no robots meta data', max_length=500, verbose_name='Robots', blank=True)),
                ('page', models.OneToOneField(related_name='extension', verbose_name='Page', to='pages.Page')),
            ],
            options={
                'verbose_name': 'page extension',
                'verbose_name_plural': 'page extensions',
            },
        ),
    ]
