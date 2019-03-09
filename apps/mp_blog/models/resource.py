from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from filer.fields.image import FilerImageField

from mptt.models import MPTTModel
from mptt.models import TreeForeignKey
from mptt.managers import TreeManager

from orderable.models import Orderable

from zinnia.managers import (DRAFT, PUBLISHED, EntryPublishedManager,
                             EntryRelatedPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)


class BaseCategory(MPTTModel):
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
        ordering = ('title',)
        abstract = True

    class MPTTMeta:
        order_insertion_by = ('title',)

    def __unicode__(self):
        return self.title


class TopicCategory(BaseCategory):
    class Meta(BaseCategory.Meta):
        verbose_name = _('topic category')
        verbose_name_plural = _('topic categories')
        abstract = False


class TypeCategory(BaseCategory):
    css_class = models.SlugField(_('CSS class'), max_length=255, blank=True)

    class Meta(BaseCategory.Meta):
        verbose_name = _('type category')
        verbose_name_plural = _('type categories')
        abstract = False


class IndustryCategory(BaseCategory):
    class Meta(BaseCategory.Meta):
        verbose_name = _('industry category')
        verbose_name_plural = _('industry categories')
        abstract = False


class ResourceEntry(
        ContentEntry,
        LeadEntry,
        ExcerptEntry,
        FeaturedEntry,
        TagsEntry,
        Orderable):
    STATUS_CHOICES = (
        (DRAFT, _('draft')),
        (PUBLISHED, _('published')),
    )

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
        related_name='resource_entries',
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
        related_name='resource_entries',
        verbose_name=_('authors'))

    # categories
    topics = models.ManyToManyField(
        TopicCategory,
        blank=True,
        related_name='entries',
        verbose_name=_('topics'))
    types = models.ManyToManyField(
        TypeCategory,
        blank=True,
        related_name='entries',
        verbose_name=_('types'))
    industries = models.ManyToManyField(
        IndustryCategory,
        blank=True,
        related_name='entries',
        verbose_name=_('industries'))

    image = FilerImageField(
            verbose_name=_('Image'),
            blank=True, null=True,
            help_text=_('Featured image.'))

    image_caption = models.TextField(
        _('caption'), blank=True,
        help_text=_("Image's caption."))

    form_link = models.URLField(_('form link'), blank=True,
                                help_text=_('Form link for iframe.'))

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    objects = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        # from CoreEntry meta
        ordering = ['-featured', '-sort_order', '-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('resource entry')
        verbose_name_plural = _('resource entries')
        index_together = (
            'status',
            'creation_date',
            'start_publication',
            'end_publication',
        )
        permissions = (
            ('can_view_all_resources', 'Can view all entries'),
            ('can_change_resource_status', 'Can change status'),
        )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Set the site to SITE_ID from settings/base.py
        """
        super(ResourceEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    def get_absolute_url(self):
        """
        Builds and returns the entry's URL based on
        the slug and the creation date.
        """
        return reverse('resource_detail', args=(self.slug,))

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
    def og_tags_list(self):
        if not self.og_tags:
            return []
        return [s for s in self.og_tags.split()]

# define __unicode__ method for ManyToMany fields
ResourceEntry.sites.through.__unicode__ = lambda x: '{}'.format(x.site)
ResourceEntry.topics.through.__unicode__ = lambda x: '{}'.format(
    x.topiccategory)
ResourceEntry.types.through.__unicode__ = lambda x: '{}'.format(x.typecategory)
ResourceEntry.industries.through.__unicode__ = lambda x: '{}'.format(
    x.industrycategory)
