# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import filer.fields.image
import django.utils.timezone
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_upgrade_to_0_16'),
        ('filer', '0007_auto_20161016_1055'),
        ('sites', '0001_initial'),
        ('mp_blog', '0014_drop_auto_now_add_of_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('icon', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Category icon (badge)', null=True, verbose_name='Image')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent category', blank=True, to='mp_blog.IndustryCategory', null=True)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'verbose_name': 'industry category',
                'verbose_name_plural': 'industry categories',
            },
        ),
        migrations.CreateModel(
            name='ResourceEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(help_text='Lead paragraph', verbose_name='lead', blank=True)),
                ('excerpt', models.TextField(help_text='Used for SEO purposes.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True, help_text="Used to build the entry's URL.", unique=True, verbose_name='slug')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (2, 'published')])),
                ('start_publication', models.DateTimeField(help_text='Start date of publication.', null=True, verbose_name='start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text='End date of publication.', null=True, verbose_name='end publication', db_index=True, blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('image_caption', models.TextField(help_text="Image's caption.", verbose_name='caption', blank=True)),
                ('form_link', models.URLField(help_text='Form link for iframe.', verbose_name='form link', blank=True)),
                ('authors', models.ManyToManyField(related_name='resource_entries', verbose_name='authors', to='zinnia.Author', blank=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Featured image.', null=True, verbose_name='Image')),
                ('industries', models.ManyToManyField(related_name='entries', verbose_name='industries', to='mp_blog.IndustryCategory', blank=True)),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='resource_entries', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-featured', '-sort_order', '-creation_date'],
                'verbose_name_plural': 'resource entries',
                'verbose_name': 'resource entry',
                'permissions': (('can_view_all_resources', 'Can view all entries'), ('can_change_resource_status', 'Can change status')),
            },
        ),
        migrations.CreateModel(
            name='TopicCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('icon', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Category icon (badge)', null=True, verbose_name='Image')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent category', blank=True, to='mp_blog.TopicCategory', null=True)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'verbose_name': 'topic category',
                'verbose_name_plural': 'topic categories',
            },
        ),
        migrations.CreateModel(
            name='TypeCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('css_class', models.SlugField(max_length=255, verbose_name='CSS class', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('icon', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Category icon (badge)', null=True, verbose_name='Image')),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent category', blank=True, to='mp_blog.TypeCategory', null=True)),
            ],
            options={
                'ordering': ('title',),
                'abstract': False,
                'verbose_name': 'type category',
                'verbose_name_plural': 'type categories',
            },
        ),
        migrations.AddField(
            model_name='resourceentry',
            name='topics',
            field=models.ManyToManyField(related_name='entries', verbose_name='topics', to='mp_blog.TopicCategory', blank=True),
        ),
        migrations.AddField(
            model_name='resourceentry',
            name='types',
            field=models.ManyToManyField(related_name='entries', verbose_name='types', to='mp_blog.TypeCategory', blank=True),
        ),
        migrations.AlterIndexTogether(
            name='resourceentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication')]),
        ),
    ]
