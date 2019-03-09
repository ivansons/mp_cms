from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.managers import PageManager
from mezzanine.pages.models import Page

import widgy
from widgy.db.fields import VersionedWidgyField
from widgy.models import links
from widgy.contrib.page_builder.models import MainContent
from widgy.contrib.widgy_mezzanine.models import (
    WidgyPageMixin,
    UseForRelatedFieldsSelectRelatedManager)


class CustomPageMixin(object):
    @property
    def stylesheets(self):
        if not self.custom_stylesheets:
            return []
        return [s for s in self.custom_stylesheets.split()]

    @property
    def javascript_files(self):
        if not self.custom_scripts:
            return []
        return [s for s in self.custom_scripts.split()]

    @property
    def og_tags_list(self):
        if not self.og_tags:
            return []
        return [s for s in self.og_tags.split()]


@widgy.register
class WordPressLayout(CustomPageMixin, MainContent):
    editable = True

    body_css_class = models.CharField(verbose_name=_('Body CSS class'),
                                      max_length=255, blank=True)
    custom_stylesheets = models.TextField(verbose_name=_('Custom stylesheets'),
                                          help_text=_('One file per line'),
                                          blank=True)
    custom_scripts = models.TextField(verbose_name=_('Custom JavaScript'),
                                      help_text=_('One file per line'),
                                      blank=True)

    og_tags = models.TextField(verbose_name=_('Custom OG:Tags'),
                               help_text=_('One file per line'),
                               blank=True)

    class Meta:
        verbose_name = _('word press page')
        verbose_name_plural = _('word press pages')


@widgy.register
class NoHeaderFooterLayout(MainContent):
    class Meta:
        verbose_name = _('no header and footer')
        verbose_name_plural = _('no header and footer')


@widgy.register
class CustomNavigationLayout(CustomPageMixin, MainContent):
    editable = True

    body_css_class = models.CharField(verbose_name=_('Body CSS class'),
                                      max_length=255, blank=True)
    custom_stylesheets = models.TextField(verbose_name=_('Custom stylesheets'),
                                          help_text=_('One file per line'),
                                          blank=True)
    custom_scripts = models.TextField(verbose_name=_('Custom JavaScript'),
                                      help_text=_('One file per line'),
                                      blank=True)

    class Meta:
        verbose_name = _('custom navigation')
        verbose_name_plural = _('custom navigation')


@widgy.register
class RealEstateVerticalLayout(CustomPageMixin, MainContent):
    editable = True

    custom_stylesheets = models.TextField(verbose_name=_('Custom stylesheets'),
                                          help_text=_('One file per line'),
                                          blank=True)
    custom_scripts = models.TextField(verbose_name=_('Custom JavaScript'),
                                      help_text=_('One file per line'),
                                      blank=True)

    class Meta:
        verbose_name = _('real estate vertical page')
        verbose_name_plural = _('real estate vertical pages')


@links.register
class RawPage(WidgyPageMixin, Page):
    HTML = 'text/html'
    PLAIN_TEXT = 'text/plain'
    JSON = 'application/json'
    XML = 'application/xml'

    CONTENT_TYPE_CHOICES = (
        (HTML, _('HTML')),
        (PLAIN_TEXT, _('Plain text')),
        (JSON, _('JSON')),
        (XML, _('XML'))
    )

    root_node = VersionedWidgyField(
        site=settings.WIDGY_MEZZANINE_SITE,
        verbose_name=_('widgy content'),
        root_choices=(
            'page_builder.MainContent',
        ),
        # WidgyField used to have these as defaults.
        null=True,
        on_delete=models.SET_NULL,
    )

    response_content_type = models.CharField(
        verbose_name=_('Response content type'),
        max_length=255,
        choices=CONTENT_TYPE_CHOICES,
        default=HTML)

    class Meta:
        verbose_name = _('raw page')
        verbose_name_plural = _('raw pages')
        swappable = 'WIDGY_MEZZANINE_PAGE_MODEL'

    _base_manager = UseForRelatedFieldsSelectRelatedManager(select_related=[
        'root_node',
        'root_node__head',
        # we might not need this, if head isn't published, but we
        # probably will.
        'root_node__head__root_node',
    ])
    objects = PageManager()
