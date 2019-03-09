from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from zinnia.admin.entry import EntryAdmin
from zinnia.managers import DRAFT

from apps.common.widgets import ClearableFileInput

from ..models import CategoryExtension
from .forms import EntryAdminForm


class CategoryExtensionInline(admin.TabularInline):
    """
    CategoryExtension admin
    """
    model = CategoryExtension


class EntryCategoryAdmin(admin.ModelAdmin):
    """
    EntryCategory admin
    """
    inlines = [CategoryExtensionInline]


class ImageFieldAdminMixin(object):
    """
    Mixin overriding image field widget
    """

    formfield_overrides = {
        models.ImageField: {
            'widget': ClearableFileInput
        }
    }


class CustomEntryAdmin(ImageFieldAdminMixin,
                       EntryAdmin):
    """
    Enrich the default EntryAdmin with CKEditor.
    """
    form = EntryAdminForm

    fieldsets = (
        (_('Content'), {
            'fields': (('title', 'status'), 'lead', 'content',)}),
        (_('Illustration'), {
            'fields': ('image', 'image_caption'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Publication'), {
            'fields': (('start_publication', 'end_publication'),
                       'creation_date'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Discussions'), {
            'fields': ('comment_enabled', 'pingback_enabled',
                       'trackback_enabled'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Privacy'), {
            'fields': ('login_required', 'password'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Templates'), {
            'fields': ('content_template', 'detail_template'),
            'classes': ('collapse', 'collapse-closed')}),
        (_('Metadatas'), {
            'fields': ('featured', 'excerpt', 'authors',
                       'display_author', 'related'),
            'classes': ('collapse', 'collapse-closed')}),
        (None, {'fields': ('categories', 'tags', 'slug')}))

    # Custom Methods
    def get_queryset(self, request):
        """
        Make special filtering by user's permissions.
        """
        if not request.user.has_perm('zinnia.can_view_all'):
            queryset = self.model.objects.filter(
                authors__pk=request.user.pk,
                status=DRAFT
            )
        else:
            queryset = super(EntryAdmin, self).get_queryset(request)
        return queryset.prefetch_related('categories', 'authors', 'sites')
