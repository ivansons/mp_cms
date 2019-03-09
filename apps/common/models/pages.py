from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from mezzanine.pages.models import Page, Link


class PageExtension(models.Model):
    """
    Page extension
    """
    page = models.OneToOneField(Page, verbose_name=_('Page'),
                                related_name='extension')
    # used to displace text underneath menu title (for navigation)
    subtitle = models.CharField(max_length=500, blank=True)
    popup = models.BooleanField(default=False)
    _meta_robots = models.CharField(
        _('Robots'), blank=True, max_length=500, default='',
        help_text=_('Optional robots data to be used in the HTML meta data. '
                    'If left blank, there will be no robots meta data'))
    allow_iframe = models.NullBooleanField(
        _('Allow iframe embedding'), help_text=_(mark_safe(
            'Unknown: system default<br />'
            'Yes: allow iframe requests (no "X-Frame-Options" header)<br />'
            'No: deny iframe requests (set "X-Frame-Options" to "DENY")')))
    meta_custom = models.TextField(
        verbose_name=_('Custom HTML content in head (extra)'),
        help_text=_('Raw HTML'), blank=True)

    class Meta:
        """
        PageExtension's meta information.
        """
        verbose_name = _('extension')
        verbose_name_plural = _('extensions')

    def __unicode__(self):
        return '{}'.format(self.page)

    @property
    def meta_robots(self):
        return self._meta_robots
