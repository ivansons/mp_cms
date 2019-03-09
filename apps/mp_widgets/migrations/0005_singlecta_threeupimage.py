# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0004_auto_20160126_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('css_class', models.CharField(default=b'inside', max_length=255, verbose_name='CSS class', blank=True)),
            ],
            options={
                'verbose_name': 'Single CTA',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ThreeUpImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
            ],
            options={
                'verbose_name': '3-up image',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='imagetitletextcta',
            options={'verbose_name': 'Image content block'},
        ),
    ]
