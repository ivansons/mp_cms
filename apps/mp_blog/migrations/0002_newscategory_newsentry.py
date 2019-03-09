# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import mptt.fields
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('zinnia', '0001_initial'),
        ('sites', '0001_initial'),
        ('mp_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(help_text="Used to build the category's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent category', blank=True, to='mp_blog.NewsCategory', null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
            },
        ),
        migrations.CreateModel(
            name='NewsEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(help_text='Lead paragraph', verbose_name='lead', blank=True)),
                ('excerpt', models.TextField(help_text='Used for SEO purposes.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='title', blank=True)),
                ('slug', models.SlugField(max_length=255, blank=True, help_text="Used to build the entry's URL.", unique=True, verbose_name='slug')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (1, 'hidden'), (2, 'published')])),
                ('start_publication', models.DateTimeField(help_text='Start date of publication.', null=True, verbose_name='start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text='End date of publication.', null=True, verbose_name='end publication', db_index=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('image_caption', models.TextField(help_text="Image's caption.", verbose_name='caption', blank=True)),
                ('video_link', models.URLField(max_length=255, verbose_name='video link', blank=True)),
                ('icon_alt_text', models.CharField(help_text='Alternate text if icon cannot be shown.', max_length=255, verbose_name='icon alternate text', blank=True)),
                ('external_link', models.URLField(max_length=255, verbose_name='external link', blank=True)),
                ('external_author', models.CharField(max_length=255, verbose_name='external author', blank=True)),
                ('external_author_url', models.URLField(max_length=255, verbose_name='external author URL', blank=True)),
                ('comment_enabled', models.BooleanField(default=True, help_text='Allows comments if checked.', verbose_name='comments enabled')),
                ('pingback_enabled', models.BooleanField(default=True, help_text='Allows pingbacks if checked.', verbose_name='pingbacks enabled')),
                ('trackback_enabled', models.BooleanField(default=True, help_text='Allows trackbacks if checked.', verbose_name='trackbacks enabled')),
                ('comment_count', models.IntegerField(default=0, verbose_name='comment count')),
                ('pingback_count', models.IntegerField(default=0, verbose_name='pingback count')),
                ('trackback_count', models.IntegerField(default=0, verbose_name='trackback count')),
                ('authors', models.ManyToManyField(related_name='news_entries', verbose_name='authors', to='zinnia.Author', blank=True)),
                ('categories', models.ManyToManyField(related_name='entries', verbose_name='categories', to='mp_blog.NewsCategory', blank=True)),
                ('icon', filer.fields.image.FilerImageField(related_name='newsentry_icon', blank=True, to='filer.Image', help_text='Icon image at the top of the preview.', null=True, verbose_name='icon')),
                ('image', filer.fields.image.FilerImageField(related_name='newsentry_image', blank=True, to='filer.Image', help_text='Featured image.', null=True, verbose_name='Image')),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='news_entries', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-creation_date'],
                'verbose_name_plural': 'news entries',
                'verbose_name': 'news entry',
                'permissions': (('can_view_all', 'Can view all entries'), ('can_change_status', 'Can change status'), ('can_change_author', 'Can change author(s)')),
            },
        ),
        migrations.AlterIndexTogether(
            name='newsentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication'), ('slug', 'creation_date')]),
        ),
    ]
