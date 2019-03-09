# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('zinnia', '0001_initial'),
        ('mp_blog', '0004_add_permissions_to_model_entry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.OneToOneField(verbose_name='Category', to='zinnia.Category')),
                ('overlay_image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Overlay image.', null=True, verbose_name='Overlay image')),
            ],
            options={
                'ordering': ['category__title'],
                'verbose_name': 'category extension',
                'verbose_name_plural': 'category extensions',
            },
        ),
    ]
