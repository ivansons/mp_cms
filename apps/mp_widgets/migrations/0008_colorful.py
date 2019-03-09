# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0007_sixup_sixupcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerstoryslide',
            name='customer_quote_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='customerstoryvideoslide',
            name='customer_quote_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='singlequote',
            name='subtitle_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.AddField(
            model_name='singlequote',
            name='title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='customerstories',
            name='background_color',
        ),
        migrations.AddField(
            model_name='customerstories',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='customerstories',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='customerstories',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='background_color',
        ),
        migrations.AddField(
            model_name='featuresection',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='featuresectionvideo',
            name='background_color',
        ),
        migrations.AddField(
            model_name='featuresectionvideo',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='sixup',
            name='background_color',
        ),
        migrations.AddField(
            model_name='sixup',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='sixup',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='sixup',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='sixup',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='sixup',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='stats',
            name='background_color',
        ),
        migrations.AddField(
            model_name='stats',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='stats',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='stats',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='stats',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='stats',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupicon',
            name='background_color',
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupicon',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupicon',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='threeupicon',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupimage',
            name='background_color',
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupimage',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupimage',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='threeupimage',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeuplongtext',
            name='background_color',
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeuplongtext',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeuplongtext',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='threeuplongtext',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupoverlay',
            name='background_color',
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupoverlay',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='threeupoverlay',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='threeupoverlay',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='titletextcta',
            name='text_color',
        ),
        migrations.AddField(
            model_name='titletextcta',
            name='text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='titletextcta',
            name='title_color',
        ),
        migrations.AddField(
            model_name='titletextcta',
            name='title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='twoupoverlay',
            name='background_color',
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='background_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='twoupoverlay',
            name='main_text_color',
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='main_text_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
        migrations.RemoveField(
            model_name='twoupoverlay',
            name='main_title_color',
        ),
        migrations.AddField(
            model_name='twoupoverlay',
            name='main_title_color',
            field=colorful.fields.RGBColorField(default=b'', blank=True),
        ),
    ]
