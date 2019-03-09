# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0003_upgrade_to_0_16'),
        ('sites', '0001_initial'),
        ('mp_blog', '0017_remove_resource_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(db_index=True, blank=True)),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('lead', models.TextField(help_text='Lead paragraph', verbose_name='lead', blank=True)),
                ('excerpt', models.TextField(help_text='Used for SEO purposes.', verbose_name='excerpt', blank=True)),
                ('featured', models.BooleanField(default=False, verbose_name='featured')),
                ('tags', tagging.fields.TagField(max_length=255, verbose_name='tags', blank=True)),
                ('language', models.CharField(default='en-US', max_length=8, choices=[('af-ZA', 'af-ZA'), ('sq-AL', 'sq-AL'), ('ar-DZ', 'ar-DZ'), ('ar-BH', 'ar-BH'), ('ar-EG', 'ar-EG'), ('ar-IQ', 'ar-IQ'), ('ar-JO', 'ar-JO'), ('ar-KW', 'ar-KW'), ('ar-LB', 'ar-LB'), ('ar-LY', 'ar-LY'), ('ar-MA', 'ar-MA'), ('ar-OM', 'ar-OM'), ('ar-QA', 'ar-QA'), ('ar-SA', 'ar-SA'), ('ar-SY', 'ar-SY'), ('ar-TN', 'ar-TN'), ('ar-AE', 'ar-AE'), ('ar-YE', 'ar-YE'), ('hy-AM', 'hy-AM'), ('Cy-az-AZ', 'Cy-az-AZ'), ('Lt-az-AZ', 'Lt-az-AZ'), ('eu-ES', 'eu-ES'), ('be-BY', 'be-BY'), ('bg-BG', 'bg-BG'), ('ca-ES', 'ca-ES'), ('zh-CN', 'zh-CN'), ('zh-HK', 'zh-HK'), ('zh-MO', 'zh-MO'), ('zh-SG', 'zh-SG'), ('zh-TW', 'zh-TW'), ('zh-CHS', 'zh-CHS'), ('zh-CHT', 'zh-CHT'), ('hr-HR', 'hr-HR'), ('cs-CZ', 'cs-CZ'), ('da-DK', 'da-DK'), ('div-MV', 'div-MV'), ('nl-BE', 'nl-BE'), ('nl-NL', 'nl-NL'), ('en-AU', 'en-AU'), ('en-BZ', 'en-BZ'), ('en-CA', 'en-CA'), ('en-CB', 'en-CB'), ('en-IE', 'en-IE'), ('en-JM', 'en-JM'), ('en-NZ', 'en-NZ'), ('en-PH', 'en-PH'), ('en-ZA', 'en-ZA'), ('en-TT', 'en-TT'), ('en-GB', 'en-GB'), ('en-US', 'en-US'), ('en-ZW', 'en-ZW'), ('et-EE', 'et-EE'), ('fo-FO', 'fo-FO'), ('fa-IR', 'fa-IR'), ('fi-FI', 'fi-FI'), ('fr-BE', 'fr-BE'), ('fr-CA', 'fr-CA'), ('fr-FR', 'fr-FR'), ('fr-LU', 'fr-LU'), ('fr-MC', 'fr-MC'), ('fr-CH', 'fr-CH'), ('gl-ES', 'gl-ES'), ('ka-GE', 'ka-GE'), ('de-AT', 'de-AT'), ('de-DE', 'de-DE'), ('de-LI', 'de-LI'), ('de-LU', 'de-LU'), ('de-CH', 'de-CH'), ('el-GR', 'el-GR'), ('gu-IN', 'gu-IN'), ('he-IL', 'he-IL'), ('hi-IN', 'hi-IN'), ('hu-HU', 'hu-HU'), ('is-IS', 'is-IS'), ('id-ID', 'id-ID'), ('it-IT', 'it-IT'), ('it-CH', 'it-CH'), ('ja-JP', 'ja-JP'), ('kn-IN', 'kn-IN'), ('kk-KZ', 'kk-KZ'), ('kok-IN', 'kok-IN'), ('ko-KR', 'ko-KR'), ('ky-KZ', 'ky-KZ'), ('lv-LV', 'lv-LV'), ('lt-LT', 'lt-LT'), ('mk-MK', 'mk-MK'), ('ms-BN', 'ms-BN'), ('ms-MY', 'ms-MY'), ('mr-IN', 'mr-IN'), ('mn-MN', 'mn-MN'), ('nb-NO', 'nb-NO'), ('nn-NO', 'nn-NO'), ('pl-PL', 'pl-PL'), ('pt-BR', 'pt-BR'), ('pt-PT', 'pt-PT'), ('pa-IN', 'pa-IN'), ('ro-RO', 'ro-RO'), ('ru-RU', 'ru-RU'), ('sa-IN', 'sa-IN'), ('Cy-sr-SP', 'Cy-sr-SP'), ('Lt-sr-SP', 'Lt-sr-SP'), ('sk-SK', 'sk-SK'), ('sl-SI', 'sl-SI'), ('es-AR', 'es-AR'), ('es-BO', 'es-BO'), ('es-CL', 'es-CL'), ('es-CO', 'es-CO'), ('es-CR', 'es-CR'), ('es-DO', 'es-DO'), ('es-EC', 'es-EC'), ('es-SV', 'es-SV'), ('es-GT', 'es-GT'), ('es-HN', 'es-HN'), ('es-MX', 'es-MX'), ('es-NI', 'es-NI'), ('es-PA', 'es-PA'), ('es-PY', 'es-PY'), ('es-PE', 'es-PE'), ('es-PR', 'es-PR'), ('es-ES', 'es-ES'), ('es-UY', 'es-UY'), ('es-VE', 'es-VE'), ('sw-KE', 'sw-KE'), ('sv-FI', 'sv-FI'), ('sv-SE', 'sv-SE'), ('syr-SY', 'syr-SY'), ('ta-IN', 'ta-IN'), ('tt-RU', 'tt-RU'), ('te-IN', 'te-IN'), ('th-TH', 'th-TH'), ('tr-TR', 'tr-TR'), ('uk-UA', 'uk-UA'), ('ur-PK', 'ur-PK'), ('Cy-uz-UZ', 'Cy-uz-UZ'), ('Lt-uz-UZ', 'Lt-uz-UZ'), ('vi-VN', 'vi-VN')])),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('region', models.CharField(max_length=100, verbose_name='region')),
                ('region_title', models.CharField(max_length=150, verbose_name='region title')),
                ('region_subtitle', models.CharField(max_length=150, verbose_name='region sub-title')),
                ('region_subhead', models.CharField(max_length=150, verbose_name='region sub-head')),
                ('region_description', models.TextField()),
                ('sub_regions', models.TextField()),
                ('keywords', models.TextField()),
                ('snippet', models.TextField()),
                ('model_link_1', models.URLField(verbose_name='model link 1')),
                ('model_link_2', models.URLField(verbose_name='model link 2')),
                ('model_link_3', models.URLField(verbose_name='model link 3')),
                ('model_subtitle_1', models.CharField(max_length=255, verbose_name='model sub-title 1')),
                ('model_subtitle_2', models.CharField(max_length=255, verbose_name='model sub-title 2')),
                ('model_subtitle_3', models.CharField(max_length=255, verbose_name='model sub-title 3')),
                ('phone', models.CharField(max_length=30, blank=True)),
                ('slug', models.SlugField(help_text="Used to build the entry's URL (/_language_/3d-real-estate-photography-services/_slug_/).", max_length=255, verbose_name='slug')),
                ('status', models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='status', choices=[(0, 'draft'), (2, 'published')])),
                ('start_publication', models.DateTimeField(help_text='Start date of publication.', null=True, verbose_name='start publication', db_index=True, blank=True)),
                ('end_publication', models.DateTimeField(help_text='End date of publication.', null=True, verbose_name='end publication', db_index=True, blank=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='creation date', db_index=True)),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('authors', models.ManyToManyField(related_name='region_entries', verbose_name='authors', to='zinnia.Author', blank=True)),
                ('sites', models.ManyToManyField(help_text='Sites where the entry will be published.', related_name='region_entries', verbose_name='sites', to='sites.Site')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-featured', '-sort_order', '-creation_date'],
                'verbose_name_plural': 'region entries',
                'verbose_name': 'region entry',
                'permissions': (('can_view_all_regions', 'Can view all entries'), ('can_change_region_status', 'Can change status'), ('can_change_region_author', 'Can change author(s)')),
            },
        ),
        migrations.AlterIndexTogether(
            name='regionentry',
            index_together=set([('status', 'creation_date', 'start_publication', 'end_publication'), ('language', 'slug')]),
        ),
    ]
