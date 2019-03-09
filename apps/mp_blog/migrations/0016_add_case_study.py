# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import filer.fields.image
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_upgrade_to_0_16'),
        ('filer', '0007_auto_20161016_1055'),
        ('sites', '0001_initial'),
        ('mp_blog', '0015_add_resources'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyEntry',
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
                ('content_right', models.TextField(blank=True)),
                ('authors', models.ManyToManyField(related_name='case_study_entries', verbose_name='authors', to='zinnia.Author', blank=True)),
                ('background_image', filer.fields.image.FilerImageField(related_name='+', blank=True, to='filer.Image', help_text='Background image', null=True, verbose_name='background image')),
                ('image', filer.fields.image.FilerImageField(related_name='+', verbose_name='Image', to='filer.Image', help_text='Image (icon)')),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='case_study_entries', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-featured', '-sort_order', '-creation_date'],
                'verbose_name_plural': 'case study entries',
                'verbose_name': 'case study entry',
                'permissions': (('can_view_all_case_studies', 'Can view all entries'), ('can_change_case_study_status', 'Can change status')),
            },
        ),
        migrations.CreateModel(
            name='CaseStudyQuote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=255, blank=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('case', models.ForeignKey(related_name='quotes', to='mp_blog.CaseStudyEntry')),
            ],
            options={
                'ordering': ('-sort_order',),
            },
        ),
        migrations.AlterIndexTogether(
            name='casestudyentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication')]),
        ),
    ]
