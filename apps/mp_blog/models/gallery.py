# -*- coding: utf8 -*-
"""
Implementation for gallery.

We try to use the feature of Zinnia as much as possible to avoid re-inventing
the wheel. On the other hand, Gallery is implemented separately with the Blog
module. This will keep these modules clean and straightforward.
"""
from __future__ import absolute_import, unicode_literals

import json
from urlparse import urlparse, parse_qs

from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from filer.fields.image import FilerImageField
from filer.models import Folder

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from orderable.models import Orderable

import requests

from zinnia.managers import (DRAFT, PUBLISHED, EntryPublishedManager,
                             EntryRelatedPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)

from .. import settings
from ..utils import upload_image_to_s3


class ModelCategory(MPTTModel):
    """
    Simple model for categorizing model entries.
    """

    title = models.CharField(
        _('title'), max_length=255)

    slug = models.SlugField(
        _('slug'), unique=True, max_length=255,
        help_text=_("Used to build the category's URL."))

    description = models.TextField(
        _('description'), blank=True)

    parent = TreeForeignKey(
        'self',
        related_name='children',
        null=True, blank=True,
        verbose_name=_('parent category'))

    objects = TreeManager()
    published = EntryRelatedPublishedManager()

    class Meta:
        """
        ModelCategory's meta informations.
        """
        ordering = ['title']
        verbose_name = _('model category')
        verbose_name_plural = _('model categories')

    class MPTTMeta:
        """
        Category MPTT's meta informations.
        """
        order_insertion_by = ['title']

    def __unicode__(self):
        return self.title

    @property
    def tree_path(self):
        """
        Returns category's tree path
        by concatening the slug of his ancestors.
        """
        if self.parent_id:
            return '/'.join(
                [ancestor.slug for ancestor in self.get_ancestors()] +
                [self.slug])
        return self.slug

    def get_absolute_url(self):
        """
        Builds and returns the category's URL
        based on his tree path.
        """
        return reverse('gallery_model_in_category', args=(self.slug,))


class ModelEntry(
        ContentEntry,
        LeadEntry,
        ExcerptEntry,
        FeaturedEntry,
        TagsEntry,
        Orderable):
    """
    Model Entry
    """

    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (PUBLISHED, _('published')))

    title = models.CharField(
        _('title'), blank=True, max_length=255)

    slug = models.SlugField(
        _('slug'), blank=True, max_length=255,
        unique=True,
        help_text=_("Used to build the entry's URL."))

    status = models.PositiveSmallIntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

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
        related_name='model_entries',
        verbose_name=_('sites'),
        help_text=_('Sites where the entry will be published.'))

    creation_date = models.DateTimeField(
        _('creation date'),
        db_index=True, default=timezone.now,
        help_text=_("Used to build the entry's URL."))

    last_update = models.DateTimeField(
        _('last update'), auto_now=True)

    authors = models.ManyToManyField(
        'zinnia.Author',
        blank=True,
        related_name='model_entries',
        verbose_name=_('authors'))

    categories = models.ManyToManyField(
        ModelCategory,
        blank=True,
        related_name='entries',
        verbose_name=_('categories'))

    image = FilerImageField(
            verbose_name=_('Image'),
            blank=True, null=True,
            help_text=_('Featured image.'))

    image_caption = models.TextField(
        _('caption'), blank=True,
        help_text=_("Image's caption."))

    admin_note = models.TextField(
        _('Admin note'), blank=True,
        help_text=_('Add any administrative and NON-PUBLIC notes you might'
                    'want to associate with this model.'))

    model_link = models.URLField(
        _('Model Link'),
        help_text=_('Copy & Paste your Matterport "Model Link" from the'
                    'Sharing column of your dashboard. Make sure your model is'
                    'shared as PUBLIC!'))

    model_vr_link = models.URLField(
        _('VR Link'), blank=True,
        help_text=_('Add a model VR link to this page. Copy & Paste the full'
                    'VR URL here.'))

    model_subtitle = models.CharField(
        _('Subtitle'), blank=True, max_length=255,
        help_text=_('Include an optional text subtitle for your model. This is'
                    'seen both on the listing page(s) as well as the model'
                    'detail page.'))

    creator_link = models.URLField(
        _('Creator Link'), blank=True,
        help_text=_('Add creator link to this page. Copy & Paste the full URL '
                    'here.'))

    presenter_link = models.URLField(
        _('Presenter Link'), blank=True,
        help_text=_('Add presenter link to this page. Copy & Paste the full '
                    'URL here.'))

    model_embed_code = models.BooleanField(
        _('Embed Code'), default=True,
        help_text=_('Display Model Embed Code'))

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
        ModelEntry meta information.
        """
        # From CoreEntry meta
        ordering = ['-featured', '-sort_order', '-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('model entry')
        verbose_name_plural = _('model entries')
        index_together = [['status', 'creation_date',
                           'start_publication', 'end_publication']]
        permissions = (('can_view_all_models', 'Can view all entries'),
                       ('can_change_model_status', 'Can change status'),
                       ('can_change_model_author', 'Can change author(s)'), )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Always validate model link before saving. Set entry title and slug if
        they are blank.
        """
        self.full_clean()
        if self.refresh_model_info:
            self._load_model_info()
            self.refresh_model_info = False
        if not self.title:
            self.title = self.model_info['name'][:255]
        if not self.slug:
            self.slug = slugify(self.title)[:255]
        if not self.content:
            self.content = self.model_info['summary']
        if not self.model_vr_link and self.model_info.get('is_vr'):
            self.model_vr_link = settings.MODEL_VR_URL_FORMAT.format(self.sid)
        if not self.image:
            self.capture_image()
        self.move_cover_image_to_folder()
        super(ModelEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        return reverse('gallery_model_detail', args=(self.slug,))

    @property
    def is_visible(self):
        """
        Checks if an entry is visible and published.
        """
        return self.is_actual and self.status == PUBLISHED

    @property
    def is_actual(self):
        """
        Checks if an entry is within his publication period.
        """
        now = timezone.now()
        if self.start_publication and now < self.start_publication:
            return False

        if self.end_publication and now >= self.end_publication:
            return False
        return True

    @property
    def publication_date(self):
        """
        Return the publication date of the entry.
        """
        return self.start_publication or self.creation_date

    @cached_property
    def sid(self):
        """
        This property is used as a validator of model link. So it doesn't
        catch any exceptions.
        """
        parsed_url = urlparse(self.model_link)
        qs = parse_qs(parsed_url.query)
        return qs['m'][0]

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

    def _load_model_info(self, commit=False):
        url = settings.SCANMODEL_API_URL_FORMAT.format(self.sid)
        response = requests.get(url)
        self._model_info = response.content if response.status_code == 200 \
            else ''
        if commit:
            self.save()

    def capture_image(self):
        """
        Save model's image as ModelEntry's featured image.
        """
        image = upload_image_to_s3(self.model_info['image'])
        self.image = image

    def move_cover_image_to_folder(self, folder_name='3d-gallery-thumbnails'):
        if self.image:
            if not self.image.folder_id \
                    or self.image.folder.name != folder_name:
                folder, _created = Folder.objects.get_or_create(
                    name=folder_name)
                self.image.folder = folder
                self.image.save()

    def clean_fields(self, exclude=None):
        """
        Validate model url:
        1. Is model public?
        2. Get model information.
        """
        super(ModelEntry, self).clean_fields(exclude=exclude)
        # Make sure model link is SSL secured.
        # Since `model_link` is a URLField, it has been stripped and properly
        # prefixed with 'http://' or 'https://'.
        if self.model_link.lower().startswith('http://'):
            self.model_link = 'https://{}'.format(self.model_link[7:])
        try:
            self.model_info
        except (KeyError, IndexError):
            raise ValidationError(_('Please input an valid model link.'))

    @property
    def og_tags_list(self):
        if not self.og_tags:
            return []
        return [s for s in self.og_tags.split()]

# define __unicode__ method for ManyToMany fields
ModelEntry.sites.through.__unicode__ = lambda x: '{}'.format(x.site)
ModelEntry.categories.through.__unicode__ = lambda x: '{}'.format(
    x.modelcategory)
ModelEntry.authors.through.__unicode__ = lambda x: '{}'.format(x.author)
