# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_builder', '0002_add_site_to_callout'),
        ('mp_widgets', '0032_realestateverticallayout_custom_scripts_css'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomNavigationLayout',
            fields=[
                ('maincontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='page_builder.MainContent')),
                ('body_css_class', models.CharField(max_length=255, verbose_name='Body CSS class', blank=True)),
                ('custom_stylesheets', models.TextField(help_text='One file per line', verbose_name='Custom stylesheets', blank=True)),
                ('custom_scripts', models.TextField(help_text='One file per line', verbose_name='Custom JavaScript', blank=True)),
            ],
            options={
                'verbose_name': 'custom navigation',
                'verbose_name_plural': 'custom navigation',
            },
            bases=('page_builder.maincontent',),
        ),
        migrations.AlterField(
            model_name='wordpresslayout',
            name='body_css_class',
            field=models.CharField(max_length=255, verbose_name='Body CSS class', blank=True),
        ),
        migrations.AlterField(
            model_name='wordpresslayout',
            name='custom_scripts',
            field=models.TextField(help_text='One file per line', verbose_name='Custom JavaScript', blank=True),
        ),
        migrations.AlterField(
            model_name='wordpresslayout',
            name='custom_stylesheets',
            field=models.TextField(help_text='One file per line', verbose_name='Custom stylesheets', blank=True),
        ),
    ]
