from __future__ import absolute_import, unicode_literals

import json

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from filer.fields.image import FilerImageField
from orderable.models import Orderable
from zinnia.managers import (DRAFT, PUBLISHED, EntryPublishedManager,
                             EntryRelatedPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)


class RegionEntry(
        ContentEntry,
        LeadEntry,
        ExcerptEntry,
        FeaturedEntry,
        TagsEntry,
        Orderable):
    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (PUBLISHED, _('published')))
    title = models.CharField(_('title'), max_length=255)
    region = models.CharField(_('region'), max_length=100)
    region_title = models.CharField(_('region title'), max_length=150)
    region_subtitle = models.CharField(_('region sub-title'), max_length=150)
    region_subhead = models.CharField(_('region sub-head'), max_length=150)
    region_description = models.TextField()
    sub_regions = models.TextField()
    keywords = models.TextField()
    snippet = models.TextField()
    model_link_1 = models.URLField(_('model link 1'))
    model_link_2 = models.URLField(_('model link 2'))
    model_link_3 = models.URLField(_('model link 3'))
    model_subtitle_1 = models.CharField(_('model sub-title 1'), max_length=255)
    model_subtitle_2 = models.CharField(_('model sub-title 2'), max_length=255)
    model_subtitle_3 = models.CharField(_('model sub-title 3'), max_length=255)
    phone = models.CharField(max_length=30, blank=True)
    in_footer = models.BooleanField(default=False)

    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    status = models.PositiveSmallIntegerField(
        _('status'), db_index=True,
        choices=STATUS_CHOICES, default=DRAFT)

    head_content = models.TextField(
        _('head content'), help_text=_('Add content to "head" when page is rendered'),
        blank=True, null=True)

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
        related_name='region_entries',
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
        related_name='region_entries',
        verbose_name=_('authors'))

    image = FilerImageField(
            verbose_name=_('Image'),
            blank=True, null=True,
            help_text=_('Featured image.'))

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    objects = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        # From CoreEntry meta
        ordering = ('-featured', '-sort_order', '-creation_date')
        get_latest_by = 'creation_date'
        verbose_name = _('region entry')
        verbose_name_plural = _('region entries')
        index_together = ('status', 'creation_date', 'start_publication',
                          'end_publication')
        permissions = (('can_view_all_regions', 'Can view all entries'),
                       ('can_change_region_status', 'Can change status'),
                       ('can_change_region_author', 'Can change author(s)'))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Always validate model link before saving. Set entry title and slug if
        they are blank.
        """
        self.full_clean()
        super(RegionEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        return reverse('region_detail', args=(self.slug,))

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

    @property
    def og_tags_list(self):
        if not self.og_tags:
            return []
        return [s for s in self.og_tags.split()]

    @cached_property
    def sub_regions_to_list(self):
        return [sub_region.strip()
                for sub_region in self.sub_regions.strip().split(',')]

    @cached_property
    def sub_regions_to_json(self):
        return json.dumps([[sub_region, self.region]
                           for sub_region in self.sub_regions_to_list])

    @cached_property
    def sub_regions_to_seo_locations(self):
        return ' / '.join(self.sub_regions_to_list)


# define __unicode__ method for ManyToMany fields
RegionEntry.sites.through.__unicode__ = lambda x: '{}'.format(x.site)
RegionEntry.authors.through.__unicode__ = lambda x: '{}'.format(x.author)
