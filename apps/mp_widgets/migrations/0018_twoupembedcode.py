# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.mp_widgets.fields
import widgy.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0017_section_main_text_is_raw_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwoUpEmbedCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', apps.mp_widgets.fields.HexColorField(max_length=7, blank=True)),
                ('main_title_size', models.IntegerField(default=2, verbose_name='Main Title Size (h1~h6)', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('main_title_is_raw_html', models.BooleanField(default=False, verbose_name='Is main title raw HTML?')),
                ('text_align', models.CharField(default=b'left', max_length=32, verbose_name='Text alignment', choices=[(b'center', 'Center'), (b'left', 'Left'), (b'right', 'Right')])),
                ('embed_code_text1', models.CharField(default=b'Copy Embed Code', max_length=255, verbose_name='Embed Code Text 1', blank=True)),
                ('data_model_id1', models.CharField(max_length=255, verbose_name='Data Model ID 1', blank=True)),
                ('embed_code_text2', models.CharField(default=b'Copy Embed Code', max_length=255, verbose_name='Embed Code Text 2', blank=True)),
                ('data_model_id2', models.CharField(max_length=255, verbose_name='Data Model ID 2', blank=True)),
            ],
            options={
                'verbose_name': '2-up embed code',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
    ]
