# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('zinnia', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent category', blank=True, to='mp_blog.ModelCategory', null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ModelEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(help_text='Lead paragraph', verbose_name='lead', blank=True)),
                ('excerpt', models.TextField(help_text='Used for SEO purposes.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True, help_text="Used to build the entry's URL.", unique=True, verbose_name='slug')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')])),
                ('start_publication', models.DateTimeField(help_text='Start date of publication.', null=True, verbose_name='start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text='End date of publication.', null=True, verbose_name='end publication', db_index=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('image_caption', models.TextField(help_text="Image's caption.", verbose_name='caption', blank=True)),
                ('admin_note', models.TextField(help_text='Add any administrative and NON-PUBLIC notes you mightwant to associate with this model.', verbose_name='Admin note', blank=True)),
                ('model_link', models.URLField(help_text='Copy & Paste your Matterport "Model Link" from theSharing column of your dashboard. Make sure your model isshared as PUBLIC!', verbose_name='Model Link')),
                ('model_vr_link', models.URLField(help_text='Add a model VR link to this page. Copy & Paste the fullVR URL here.', verbose_name='Model VR Link', blank=True)),
                ('model_subtitle', models.CharField(help_text='Include an optional text subtitle for your model. This isseen both on the listing page(s) as well as the modeldetail page.', max_length=255, verbose_name='Model Subtitle', blank=True)),
                ('model_embed_code', models.BooleanField(default=True, help_text='Display Model Embed Code', verbose_name='Model Embed Code')),
                ('authors', models.ManyToManyField(related_name='model_entries', verbose_name='authors', to='zinnia.Author', blank=True)),
                ('categories', models.ManyToManyField(related_name='entries', verbose_name='categories', to='mp_blog.ModelCategory', blank=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Featured image.', null=True, verbose_name='Image')),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='model_entries', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
