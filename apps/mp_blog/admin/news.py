from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from zinnia.admin.entry import EntryAdmin
from zinnia.admin.filters import AuthorListFilter
from zinnia.managers import DRAFT, PUBLISHED
from zinnia.settings import PING_DIRECTORIES

from ..models.news import NewsEntry

from .filters import NewsCategoryListFilter
from .forms import NewsEntryAdminForm

# Code from zinnia-wysiwyg-ckeditor admin.py as it is not compatible if
# ENTRY_BASE_MODEL is extended
if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    from ckeditor_uploader.widgets import CKEditorUploadingWidget as CKEditor
else:
    from ckeditor.widgets import CKEditorWidget as CKEditor

CONFIG_NAME = 'zinnia-content'
CKEDITOR_CONFIG = getattr(settings, 'CKEDITOR_CONFIGS', {})
if CONFIG_NAME not in CKEDITOR_CONFIG:
    CONFIG_NAME = 'default'


class NewsEntryAdmin(EntryAdmin):
    form = NewsEntryAdminForm
    date_hierarchy = 'creation_date'

    fieldsets = (
        (_('News'), {
            'fields': ('icon', 'icon_alt_text', 'external_link',
                       'external_author', 'external_author_url',
                       'comment_enabled', 'status')}),
        (_('Content'), {
            'fields': (('title', 'slug'), 'lead', 'content')}),
        (None, {'fields': ('categories', 'tags')}),

        (_('Publication'), {
            'fields': (('start_publication', 'end_publication'),),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Metadata'), {
            'fields': ('featured', 'og_tags', 'excerpt', 'authors'),
            'classes': ('collapse', 'collapse-open')}))
    list_filter = (NewsCategoryListFilter, AuthorListFilter, 'status',
                   'featured', 'creation_date', 'start_publication',
                   'end_publication', 'sites')
    list_display = ('get_title', 'get_authors', 'get_categories',
                    'get_sites', 'get_is_visible', 'featured',
                    'creation_date')
    radio_fields = {}
    filter_horizontal = ('categories', 'authors')
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ('title', 'excerpt', 'content')
    actions = ['make_mine', 'make_published', 'make_hidden',
               'mark_featured', 'unmark_featured']
    actions_on_top = True
    actions_on_bottom = True

    def __init__(self, model, admin_site):
        self.form.admin_site = admin_site
        super(NewsEntryAdmin, self).__init__(model, admin_site)

    # Custom Display
    def get_title(self, entry):
        """
        Return the title with word count and number of comments.
        """
        title = _('%(title)s (%(word_count)i words)') % \
            {'title': entry.title, 'word_count': entry.word_count}
        return title
    get_title.short_description = _('title')

    # Custom Methods
    def get_queryset(self, request):
        """
        Make special filtering by user's permissions.
        """
        if not request.user.has_perm('mp_blog.can_view_all'):
            queryset = self.model.objects.filter(
                authors__pk=request.user.pk,
                status=DRAFT
            )
        else:
            queryset = super(EntryAdmin, self).get_queryset(request)
        return queryset.prefetch_related('categories', 'authors', 'sites')

    def get_readonly_fields(self, request, obj=None):
        """
        Return readonly fields by user's permissions.
        """
        readonly_fields = list(super(EntryAdmin, self).get_readonly_fields(
            request, obj))

        if not request.user.has_perm('mp_blog.can_change_status'):
            readonly_fields.append('status')

        if not request.user.has_perm('mp_blog.can_change_author'):
            readonly_fields.append('authors')

        return readonly_fields

    def get_actions(self, request):
        """
        Define actions by user's permissions.
        """
        actions = super(EntryAdmin, self).get_actions(request)
        if not actions:
            return actions
        if (not request.user.has_perm('mp_blog.can_change_author') or
                not request.user.has_perm('mp_blog.can_view_all')):
            del actions['make_mine']
        if not request.user.has_perm('mp_blog.can_change_status'):
            del actions['make_hidden']
            del actions['make_published']
        if not PING_DIRECTORIES:
            del actions['ping_directories']

        return actions

    def make_published(self, request, queryset):
        """
        Set entries selected as published.
        """
        queryset.update(status=PUBLISHED)
        self.message_user(
            request, _('The selected entries are now marked as published.'))
    make_published.short_description = _('Set entries selected as published')

    def make_hidden(self, request, queryset):
        """
        Set entries selected as hidden.
        """
        queryset.update(status=NewsEntry.HIDDEN)
        self.message_user(
            request, _('The selected entries are now marked as hidden.'))
    make_hidden.short_description = _('Set entries selected as hidden')

    def put_on_top(self, request, queryset):
        """
        Put the selected entries on top at the current date.
        """
        queryset.update(creation_date=timezone.now())
        self.message_user(request, _(
            'The selected entries are now set at the current date.'))
    put_on_top.short_description = _(
        'Put the selected entries on top at the current date')


class NewsEntryAdminCKEditorForm(NewsEntryAdminForm):
    """
    Define the CKEditor widget for the content field.
    """
    content = forms.CharField(
        label=_('Content'), required=False,
        widget=CKEditor(config_name=CONFIG_NAME))


class NewsEntryAdminCKEditorMixin(object):
    """
    Mixin adding CKEditor for editing Entry.content field.
    """
    form = NewsEntryAdminCKEditorForm


class NewsEntryCKEditorAdmin(NewsEntryAdminCKEditorMixin,
                             NewsEntryAdmin):
    """
    Enrich the default EntryAdmin with CKEditor.
    """
    pass
