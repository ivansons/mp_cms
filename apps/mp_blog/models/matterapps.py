from __future__ import absolute_import, unicode_literals

import json

from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy, reverse

from filer.fields.image import FilerImageField
from filer.models import Folder

from orderable.models import Orderable

import requests

from zinnia.managers import (DRAFT, PUBLISHED, EntryPublishedManager,
                             EntryRelatedPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)

from .. import settings
from ..utils import upload_image_to_s3

class MatterAppsEntry(
        ContentEntry,
        LeadEntry,
        ExcerptEntry,
        FeaturedEntry,
        TagsEntry,
        Orderable):
    """
    Gallery Page Entry
    """

    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (PUBLISHED, _('published')))

    CATEGORIES_CHOICES = ((1, _('Apps')),
                        (2, _('Service')),
                        (3, _('Merchandise')))

    slug = models.SlugField(
        _('slug'), blank=False, max_length=255,
        unique=True,
        help_text=_("Used to build the entry's URL."))

    title = models.CharField(
        _('title'), blank=False, max_length=255, unique=True)

    tagline = models.CharField(
        _('tagline'), blank=False, max_length=145)

    description = models.TextField(
        _('description'), blank=False, max_length=None)

    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True, null=True,
        help_text=_('Featured image.'))

    price = models.CharField(
        _('price'), blank=False, max_length=25)

    price_option = models.BooleanField(_('Starting at'), default=False)

    compatibility = models.CharField(
        _('compatibility'), blank=True, max_length=150, default='Nothing')

    status = models.PositiveSmallIntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

    category = models.PositiveSmallIntegerField(
        _('category'), db_index=False,
        choices=CATEGORIES_CHOICES, default=1)

    author = models.CharField(
        _('author name'), blank=False, max_length=60)

    author_image = FilerImageField(
        verbose_name=_('User Image'),
        blank=True, null=True,
        help_text=_('User Image Profile.'),
        related_name='author_image')

    company_name = models.CharField(
        _('company'), blank=True, null=True, max_length=150)

    company_url = models.URLField(
        _('company link'), blank=True, null=True, max_length=150, 
        help_text=_('Link to company.'))

    company_description = models.TextField(
        _('company description'), blank=True, null=True, max_length=None)

    button_text = models.CharField(
        _('button text'), max_length='150', default='Download')

    button_link = models.URLField(
        _('button link'), max_length='150', help_text=_('Go to.'))

    creation_date = models.DateTimeField(
        _('creation date'),
        db_index=True, default=timezone.now,
        help_text=_("Used to build the entry's URL."))

    start_publication = models.DateTimeField(
        _('start publication'),
        db_index=True, blank=True, null=True,
        help_text=_('Start date of publication.'))

    end_publication = models.DateTimeField(
        _('end publication'),
        db_index=True, blank=True, null=True,
        help_text=_('End date of publication.'))

    sites = models.ManyToManyField(
        Site,
        related_name='matterapps_entry',
        verbose_name=_('sites'),
        help_text=_('Sites where the entry will be published.'))

    last_update = models.DateTimeField(
        _('last update'), auto_now=True)

    # TODO: Switch to JsonField when upgrading Django to 1.9.
    _model_info = models.TextField(
        _('Model Information'), blank=True)

    refresh_model_info = models.BooleanField(
        _('Refresh model info'), default=False,
        help_text=_('Reload model info from API'))

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    objects = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        """
        MatterAppsEntry meta information.
        """
        # From CoreEntry meta
        ordering = ['-featured', '-sort_order', '-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('App Entry')
        verbose_name_plural = _('App Entries')
        index_together = [['status', 'creation_date']]
        permissions = (('can_view_all_models', 'Can view all entries'),
                       ('can_change_model_status', 'Can change status'),
                       ('can_change_model_author', 'Can change author(s)'), )

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        return reverse_lazy('matterapps_detail', kwargs={'slug': self.slug,})

    @property
    def og_tags_list(self):
        if not self.og_tags:
            return []
        return [s for s in self.og_tags.split()]

    @cached_property
    def model_info(self):
        """
        Get model information in json format through Portal API.
        """
        if not self._model_info:
            self._load_model_info()
        try:
            data = json.loads(self._model_info)
        except (TypeError, ValueError):
            data = {}
        return data

    @cached_property
    def time_created(self):
        return parse_datetime(self.model_info['created'])

    def move_cover_image_to_folder(self, folder_name='matterapps-thumbnails'):
        if self.image:
            if not self.image.folder_id \
                    or self.image.folder.name != folder_name:
                folder, _created = Folder.objects.get_or_create(
                    name=folder_name)
                self.image.folder = folder
                self.image.save()

        if self.author_image:
            if not self.author_image.folder_id \
                    or self.author_image.folder.name != folder_name:
                folder, _created = Folder.objects.get_or_create(
                    name=folder_name)
                self.author_image.folder = folder
                self.author_image.save()
