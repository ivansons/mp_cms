# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0033_customnavigationlayout_remove_default_from_wordpresslayout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, blank=True)),
                ('description', models.CharField(default=b'Description', max_length=255, blank=True)),
                ('delay', models.IntegerField(default=5, help_text='How many seconds delay to show popup?')),
                ('recurrence', models.IntegerField(default=3, help_text='Days of recurrence (0 means never).')),
                ('cookie_name', models.CharField(help_text='Identify popup widgets across pages.', max_length=50, blank=True)),
            ],
            options={
                'verbose_name': 'popup widget',
            },
        ),
    ]
