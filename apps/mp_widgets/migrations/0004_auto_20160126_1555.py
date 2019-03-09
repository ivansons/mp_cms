# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import widgy.models.mixins
import widgy.contrib.page_builder.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0003_customerstories_customerstoryslide_customerstoryvideoslide_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTitleTextCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'icon image block',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='iconimagetitletextcta',
            name='image',
        ),
        migrations.RemoveField(
            model_name='longtextimagetitletextcta',
            name='image',
        ),
        migrations.RemoveField(
            model_name='overlayimagetitletextcta',
            name='image',
        ),
        migrations.DeleteModel(
            name='IconImageTitleTextCta',
        ),
        migrations.DeleteModel(
            name='LongTextImageTitleTextCta',
        ),
        migrations.DeleteModel(
            name='OverlayImageTitleTextCta',
        ),
    ]
