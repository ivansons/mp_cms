from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from filer.fields.image import FilerImageField
from orderable.models import Orderable
from zinnia.managers import (DRAFT, PUBLISHED, EntryPublishedManager)
from zinnia.models_bases.entry import (ContentEntry, FeaturedEntry, LeadEntry,
                                       ExcerptEntry, TagsEntry)


class CaseStudyEntry(
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
        related_name='case_study_entries',
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
        related_name='case_study_entries',
        verbose_name=_('authors'))

    image = FilerImageField(verbose_name=_('Image'),
                            help_text=_('Image (icon)'),
                            related_name='+')
    image_caption = models.TextField(_('caption'),
                                     help_text=_("Image's caption."),
                                     blank=True)
    background_image = FilerImageField(verbose_name=_('background image'),
                                       help_text=_('Background image'),
                                       related_name='+',
                                       blank=True, null=True)

    content_right = models.TextField(blank=True)

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    objects = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        # from CoreEntry meta
        ordering = ['-featured', '-sort_order', '-creation_date']
        get_latest_by = 'creation_date'
        verbose_name = _('case study entry')
        verbose_name_plural = _('case study entries')
        index_together = (
            'status',
            'creation_date',
            'start_publication',
            'end_publication',
        )
        permissions = (
            ('can_view_all_case_studies', 'Can view all entries'),
            ('can_change_case_study_status', 'Can change status'),
        )

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(CaseStudyEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    def get_absolute_url(self):
        return reverse('case_study_detail', args=(self.slug,))

    @property
    def is_visible(self):
        return self.is_actual and self.status == PUBLISHED

    @property
    def is_actual(self):
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


class CaseStudyQuote(Orderable):
    case = models.ForeignKey(CaseStudyEntry, related_name='quotes')
    content = models.TextField()
    name = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ('-sort_order',)

    def __unicode__(self):
        return 'Quote by {} for {}'.format(self.name, self.case)
