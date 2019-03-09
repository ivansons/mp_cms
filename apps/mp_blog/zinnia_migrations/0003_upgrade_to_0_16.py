# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


def fill_publication_date(apps, schema_editor):
    Entry = apps.get_model('zinnia', 'Entry')
    for entry in Entry.objects.all():
        entry.publication_date = entry.creation_date
        entry.save()


def unfill_publication_date(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0002_entry_display_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-publication_date'], 'get_latest_by': 'publication_date', 'verbose_name': 'entry', 'verbose_name_plural': 'entries', 'permissions': (('can_view_all', 'Can view all entries'), ('can_change_status', 'Can change status'), ('can_change_author', 'Can change author(s)'))},
        ),
        migrations.AddField(
            model_name='entry',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text="Used to build the entry's URL.", verbose_name='publication date', db_index=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='slug',
            field=models.SlugField(help_text="Used to build the entry's URL.", max_length=255, verbose_name='slug', unique_for_date=b'publication_date'),
        ),
        migrations.AlterIndexTogether(
            name='entry',
            index_together=set([('slug', 'publication_date'), ('status', 'publication_date', 'start_publication', 'end_publication')]),
        ),
        migrations.RunPython(fill_publication_date, unfill_publication_date),
    ]
