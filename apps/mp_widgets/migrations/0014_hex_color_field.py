# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.mp_widgets.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0013_column_row'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerstories',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='customerstories',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='customerstoryslide',
            name='customer_quote_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='customerstoryvideoslide',
            name='customer_quote_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='featuresection',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='featuresectionvideo',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='singlequote',
            name='subtitle_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='singlequote',
            name='title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sixup',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sixup',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='sixup',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='stats',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupicon',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupicon',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupicon',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupimage',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupimage',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupimage',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeuplongtext',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeuplongtext',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeuplongtext',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupoverlay',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupoverlay',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='threeupoverlay',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='titletextcta',
            name='text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='titletextcta',
            name='title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='twoupoverlay',
            name='background_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='twoupoverlay',
            name='main_text_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
        migrations.AlterField(
            model_name='twoupoverlay',
            name='main_title_color',
            field=apps.mp_widgets.fields.HexColorField(max_length=7, blank=True),
        ),
    ]
