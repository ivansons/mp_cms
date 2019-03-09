# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0012_nav_tab_panel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('width', models.CharField(default=b'1/2', max_length=50, verbose_name='Column width', choices=[(b'1/3', '1/3 of row'), (b'1/2', '1/2 of row'), (b'2/3', '2/3 of row')])),
            ],
            options={
                'verbose_name': 'Column in row',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Row container',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
    ]
