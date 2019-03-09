# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mp_blog', '0010_modelentry_sort_order_initialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelentry',
            name='creator_link',
            field=models.URLField(help_text='Add creator link to this page. Copy & Paste the full URL here.', verbose_name='Creator Link', blank=True),
        ),
        migrations.AddField(
            model_name='modelentry',
            name='presenter_link',
            field=models.URLField(help_text='Add presenter link to this page. Copy & Paste the full URL here.', verbose_name='Presenter Link', blank=True),
        ),
        migrations.AlterField(
            model_name='modelentry',
            name='model_embed_code',
            field=models.BooleanField(default=True, help_text='Display Model Embed Code', verbose_name='Embed Code'),
        ),
        migrations.AlterField(
            model_name='modelentry',
            name='model_subtitle',
            field=models.CharField(help_text='Include an optional text subtitle for your model. This isseen both on the listing page(s) as well as the modeldetail page.', max_length=255, verbose_name='Subtitle', blank=True),
        ),
        migrations.AlterField(
            model_name='modelentry',
            name='model_vr_link',
            field=models.URLField(help_text='Add a model VR link to this page. Copy & Paste the fullVR URL here.', verbose_name='VR Link', blank=True),
        ),
    ]
