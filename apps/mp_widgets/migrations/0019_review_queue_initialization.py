# -*- coding: utf-8 -*-
"""
Review queue database initialization

Upgrading from a non-reviewed site, a widgy.contrib.review_queue.models.
ReviewedVersionCommit object must be created for each widgy.models.
VersionCommit.
"""
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # create `ReviewedVersionCommit` objects
    VersionCommit = apps.get_model('widgy', 'VersionCommit')
    ReviewedVersionCommit = apps.get_model('review_queue', 'ReviewedVersionCommit')

    for commit in VersionCommit.objects.filter(reviewedversioncommit=None):
        new_commit = ReviewedVersionCommit(
            versioncommit_ptr=commit,
            approved_at=commit.created_at,
            approved_by_id=commit.author_id,
        )
        new_commit.__dict__.update(commit.__dict__)
        new_commit.save()


def reverse_func(apps, schema_editor):
    # delete `ReviewedVersionCommit` objects
    ReviewedVersionCommit = apps.get_model('review_queue', 'ReviewedVersionCommit')
    ReviewedVersionCommit.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mp_widgets', '0018_twoupembedcode'),
        ('review_queue', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
