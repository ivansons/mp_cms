# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import widgy.models.mixins
import widgy.contrib.page_builder.db.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('mp_widgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(default=b'CTA text', max_length=255, verbose_name='CTA text', blank=True)),
                ('url', models.CharField(default=b'CTA url', max_length=255, verbose_name='CTA url', blank=True)),
            ],
            options={
                'verbose_name': 'CTA',
            },
        ),
        migrations.CreateModel(
            name='FeatureSectionVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('text_content_is_on_left', models.BooleanField(default=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
                ('video', widgy.contrib.page_builder.db.fields.VideoField(help_text='Please enter a link to the YouTube or Vimeo page for this video.  i.e. http://www.youtube.com/watch?v=9bZkp7q19f0', null=True, verbose_name='Video', blank=True)),
                ('background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'feature section video',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IconImageTitleTextCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'icon image block',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='LongTextImageTitleTextCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'long text image block',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='OverlayImageTitleTextCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'overlay image block',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_image', widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Background image', blank=True, to='filer.File', null=True)),
            ],
            options={
                'verbose_name': 'quotes',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SingleQuote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, verbose_name='Title', blank=True)),
                ('subtitle', models.CharField(default=b'Sub-title', max_length=255, verbose_name='Sub-title', blank=True)),
            ],
            options={
                'verbose_name': 'single quote',
            },
        ),
        migrations.CreateModel(
            name='ThreeCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': '3 CTA',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ThreeUpIcon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
            ],
            options={
                'verbose_name': '3-up icon',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ThreeUpLongText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
            ],
            options={
                'verbose_name': '3-up long text',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ThreeUpOverlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
            ],
            options={
                'verbose_name': '3-up overlay',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TitleTextCta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'Title', max_length=255, blank=True)),
                ('title_color', models.CharField(default=b'', max_length=255, blank=True)),
                ('title_size', models.IntegerField(default=2, null=True, blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('text_is_raw_html', models.BooleanField(default=False)),
                ('text', models.TextField(default=b'Text', blank=True)),
                ('text_color', models.CharField(default=b'', max_length=255, blank=True)),
            ],
            options={
                'verbose_name': 'title text block',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.CreateModel(
            name='TwoUpOverlay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('background_color', models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True)),
                ('main_title', models.CharField(default=b'Main Title', max_length=255, verbose_name='Main title', blank=True)),
                ('main_title_color', models.CharField(default=b'', max_length=255, verbose_name='Main title color', blank=True)),
                ('main_text', models.CharField(default=b'Main Text', max_length=1000, verbose_name='Main text', blank=True)),
                ('main_text_color', models.CharField(default=b'', max_length=255, verbose_name='Main text color', blank=True)),
                ('css_class', models.CharField(default=b'', max_length=255, verbose_name='CSS class', blank=True)),
                ('css_style', models.TextField(default=b'', verbose_name='CSS style', blank=True)),
            ],
            options={
                'verbose_name': '2-up overlay',
            },
            bases=(widgy.models.mixins.DefaultChildrenMixin, models.Model),
        ),
        migrations.RenameField(
            model_name='featuresection',
            old_name='content_is_on_left',
            new_name='text_content_is_on_left',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='hyperlink1_text',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='hyperlink1_url',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='hyperlink2_text',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='hyperlink2_url',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='text',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='text_is_raw_html',
        ),
        migrations.RemoveField(
            model_name='featuresection',
            name='title',
        ),
        migrations.AddField(
            model_name='featuresection',
            name='background_color',
            field=models.CharField(default=b'', max_length=255, verbose_name='Background color', blank=True),
        ),
        migrations.AlterField(
            model_name='featuresection',
            name='background_image',
            field=widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Background image', blank=True, to='filer.File', null=True),
        ),
        migrations.AlterField(
            model_name='featuresection',
            name='css_style',
            field=models.TextField(default=b'', verbose_name='CSS style', blank=True),
        ),
        migrations.AlterField(
            model_name='featuresection',
            name='foreground_image',
            field=widgy.contrib.page_builder.db.fields.ImageField(related_name='+', on_delete=django.db.models.deletion.PROTECT, verbose_name='Foreground image', blank=True, to='filer.File', null=True),
        ),
    ]
