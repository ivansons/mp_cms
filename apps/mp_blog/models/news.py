# -*- coding: utf8 -*-
"""
Implementation for news.

We try to use the feature of Zinnia as much as possible to avoid re-inventing
the wheel. On the other hand, News is implemented separately with the Blog
module. This will keep these modules clean and straightforward.
"""
from __future__ import absolute_import

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from filer.fields.image import FilerImageField

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from zinnia.managers import (DRAFT, HIDDEN, PUBLISHED, EntryPublishedManager,
                             EntryRelatedPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)


class NewsCategory(MPTTModel):
    """
    Simple model for News category
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
        NewsCategory meta information.
        """
        ordering = ['title']
        verbose_name = _('news category')
        verbose_name_plural = _('news categories')

    class MPTTMeta:
        """
        Category MPTT meta information.
        """
        order_insertion_by = ['title']

    def __unicode__(self):
        return self.title

    @property
    def tree_path(self):
        """
        Returns category's tree path
        by concatenating the slug of his ancestors.
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
        return reverse('news_category_detail', args=(self.slug,))


class NewsEntry(
        ContentEntry,
        LeadEntry,
        ExcerptEntry,
        FeaturedEntry,
        TagsEntry):

    STATUS_CHOICES = ((DRAFT, _('draft')),
                      (HIDDEN, _('hidden')),
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
        related_name='news_entries',
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
        related_name='news_entries',
        verbose_name=_('authors'))

    categories = models.ManyToManyField(
        NewsCategory,
        blank=True,
        related_name='entries',
        verbose_name=_('categories'))

    image = FilerImageField(
        verbose_name=_('Image'),
        blank=True, null=True, related_name='newsentry_image',
        help_text=_('Featured image.'))

    image_caption = models.TextField(
        _('caption'), blank=True,
        help_text=_("Image's caption."))

    # News fields based on WP site
    video_link = models.URLField(
        _('embed video link'), blank=True, max_length=255,
        help_text=_('How to get embedded links: '
                    '<a href="https://support.google.com/youtube/answer/171780?hl=en" target="_blank">YouTube</a>, '
                    '<a href="https://vimeo.com/help/faq/sharing-videos/embedding-videos#how-do-i-embed-a-video-on-another-site" target="_blank">Vimeo</a>. '
                    'If you need assistance embedding a video from another '
                    'website contact your site administrator.<br>'
                    'Vimeo link example: '
                    'https://player.vimeo.com/video/157326630'))

    icon = FilerImageField(
        verbose_name=_('icon'),
        blank=True, null=True, related_name='newsentry_icon',
        help_text=_('Icon image at the top of the preview.'))

    icon_alt_text = models.CharField(
        _('icon alternate text'), blank=True, max_length=255,
        help_text=_('Alternate text if icon cannot be shown.'))

    external_link = models.URLField(
        _('external link'), blank=True, max_length=255)

    external_author = models.CharField(
        _('external author'), blank=True, max_length=255)

    external_author_url = models.URLField(
        _('external author URL'), blank=True, max_length=255)

    # Fields for comments, trackbacks and pingbacks
    comment_enabled = models.BooleanField(
        _('comments enabled'), default=True,
        help_text=_('Allows comments if checked.'))

    pingback_enabled = models.BooleanField(
        _('pingbacks enabled'), default=True,
        help_text=_('Allows pingbacks if checked.'))

    trackback_enabled = models.BooleanField(
        _('trackbacks enabled'), default=True,
        help_text=_('Allows trackbacks if checked.'))

    comment_count = models.IntegerField(
        _('comment count'), default=0)

    pingback_count = models.IntegerField(
        _('pingback count'), default=0)

    trackback_count = models.IntegerField(
        _('trackback count'), default=0)

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    objects = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        """
        NewsEntry meta information.
        """
        # From CoreEntry meta
        ordering = ['-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('news entry')
        verbose_name_plural = _('news entries')
        index_together = [['slug', 'creation_date'],
                          ['status', 'creation_date',
                           'start_publication', 'end_publication']]
        permissions = (('can_view_all', 'Can view all entries'),
                       ('can_change_status', 'Can change status'),
                       ('can_change_author', 'Can change author(s)'), )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Set the site to SITE_ID from settings/base.py
        """
        super(NewsEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        return reverse('news_detail', args=(self.slug,))

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


# define __unicode__ method for ManyToMany fields
NewsEntry.sites.through.__unicode__ = lambda x: '{}'.format(x.site)
NewsEntry.categories.through.__unicode__ = lambda x: '{}'.format(
    x.newscategory)
NewsEntry.authors.through.__unicode__ = lambda x: '{}'.format(x.author)
