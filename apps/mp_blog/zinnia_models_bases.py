import os

from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from zinnia.models_bases.entry import AbstractEntry
from zinnia.settings import UPLOAD_TO

BLOG_TYPE_CHOICES = (('Regular Blog', 'Regular'), ('News', 'News'))


class BlogAbstractEntry(AbstractEntry):
    """
    Abstract base class for Matterport Zinnia Blog Entry
    """
    # blog_type = models.CharField(max_length=255,
    #                              default=BLOG_TYPE_CHOICES[0][0],
    #                              choices=BLOG_TYPE_CHOICES)
    #
    # thumbnail = models.ImageField(blank=True, null=True)

    display_author = models.CharField(
        _('Display author'), max_length=255, blank=True)

    class Meta(AbstractEntry.Meta):
        abstract = True

    def __str__(self):
        return u'BlogEntry %s' % self.title

    def image_upload_to(self, filename):
        """
        Compute the upload path for the image field.
        """
        now = timezone.now()
        filename, extension = os.path.splitext(filename)

        fullpath = os.path.join(
            UPLOAD_TO,
            now.strftime('%Y'),
            now.strftime('%m'),
            now.strftime('%d'),
            slugify(filename)
        )

        return u'{}{}'.format(
            fullpath[:100-len(extension)],
            extension
        )

    def save(self, *args, **kwargs):
        """
        Set the site to SITE_ID from settings/base.py
        """
        super(BlogAbstractEntry, self).save(*args, **kwargs)
        self.sites.add(Site.objects.get_current())

    @cached_property
    def category_overlay(self):
        # use `self.categories.all` instead of `self.categories.filter()` to
        # use the cached query results of categories.
        for category in self.categories.all():
            try:
                if category.categoryextension.overlay_image:
                    return category.categoryextension.overlay_image
            except ObjectDoesNotExist:
                pass
        return None
