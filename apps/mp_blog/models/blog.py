# -*- coding: utf8 -*-
"""
Extension for zinnia blog.
"""
from __future__ import absolute_import

from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from zinnia.models import Category, Entry


class CategoryExtension(models.Model):
    """
    Category extension
    """
    category = models.OneToOneField(Category, verbose_name=_('Category'))
    overlay_image = FilerImageField(
        verbose_name=_('Overlay image'),
        blank=True,
        null=True,
        help_text=_('Overlay image.')
    )

    class Meta:
        """
        CategoryExtension's meta information.
        """
        ordering = ['category__title']
        verbose_name = _('category extension')
        verbose_name_plural = _('category extensions')

    def __unicode__(self):
        return u'{}'.format(self.category)


# define __unicode__ method for ManyToMany fields
Entry.sites.through.__unicode__ = lambda x: '{}'.format(x.site)
Entry.categories.through.__unicode__ = lambda x: '{}'.format(x.category)
Entry.authors.through.__unicode__ = lambda x: '{}'.format(x.author)
Entry.related.through.__unicode__ = lambda x: '{}'.format(x.from_entry)
