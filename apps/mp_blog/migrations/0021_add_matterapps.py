# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import filer.fields.image
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('sites', '0001_initial'),
        ('mp_blog', '0020_regionentry_in_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatterAppsEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(help_text='Lead paragraph', verbose_name='lead', blank=True)),
                ('excerpt', models.TextField(help_text='Used for SEO purposes.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('slug', models.SlugField(help_text="Used to build the entry's URL.", unique=True, max_length=255, verbose_name='slug')),
                ('title', models.CharField(unique=True, max_length=255, verbose_name='title')),
                ('tagline', models.CharField(max_length=145, verbose_name='tagline')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.CharField(max_length=25, verbose_name='price')),
                ('compatibility', models.CharField(default='Nothing', max_length=150, verbose_name='compatibility')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (2, 'published')])),
                ('category', models.PositiveSmallIntegerField(default=1, verbose_name='category', choices=[(1, 'Apps'), (2, 'Service'), (3, 'Merchandise')])),
                ('author', models.CharField(max_length=60, verbose_name='author name')),
                ('company_name', models.CharField(max_length=150, verbose_name='company')),
                ('company_url', models.URLField(help_text='Link to company.', max_length=150, verbose_name='company link')),
                ('company_description', models.TextField(verbose_name='company description')),
                ('button_text', models.CharField(default='Download', max_length='150', verbose_name='button text')),
                ('button_link', models.URLField(help_text='Go to.', max_length='150', verbose_name='button link')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True)),
                ('start_publication', models.DateTimeField(help_text='Start date of publication.', null=True, verbose_name='start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text='End date of publication.', null=True, verbose_name='end publication', db_index=True, blank=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('_model_info', models.TextField(verbose_name='Model Information', blank=True)),
                ('refresh_model_info', models.BooleanField(default=False, help_text='Reload model info from API', verbose_name='Refresh model info')),
                ('author_image', filer.fields.image.FilerImageField(related_name='author_image', blank=True, to='filer.Image', help_text='User Image Profile.', null=True, verbose_name='User Image')),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', help_text='Featured image.', null=True, verbose_name='Image')),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='matterapps_entry', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-featured', '-sort_order', '-creation_date'],
                'verbose_name_plural': 'App Entries',
                'verbose_name': 'App Entry',
                'permissions': (('can_view_all_models', 'Can view all entries'), ('can_change_model_status', 'Can change status'), ('can_change_model_author', 'Can change author(s)')),
            },
        ),
        migrations.AlterIndexTogether(
            name='matterappsentry',
            index_together=set([('status', 'creation_date')]),
        ),
]