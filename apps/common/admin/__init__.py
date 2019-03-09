from __future__ import absolute_import

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, LinkAdmin
from mezzanine.pages.models import Page, RichTextPage, Link
from widgy.contrib.widgy_mezzanine import get_widgypage_model
from widgy.contrib.widgy_mezzanine.admin import WidgyPageAdmin
from filer.admin.folderadmin import FolderAdmin
from filer.models import Folder

from ..models import PageExtension

WidgyPage = get_widgypage_model()


class PageExtensionInline(admin.TabularInline):
    """
    PageExtension admin
    """
    model = PageExtension


class CustomPageAdmin(PageAdmin):
    """
    Page admin with inline page extension
    """
    inlines = (PageExtensionInline,)


class CustomWidgyPageAdmin(WidgyPageAdmin):
    """
    WidgyPage admin with inline page extension
    """
    inlines = (PageExtensionInline,)


class CustomLinkAdmin(LinkAdmin):
    """
    Page admin with inline page extension
    """
    inlines = (PageExtensionInline,)


class CustomFilerFolderAdmin(FolderAdmin):
    def get_actions(self, request):
        actions = super(CustomFilerFolderAdmin, self).get_actions(request)
        if 'files_set_public' in actions:
            del actions['files_set_public']
        if 'files_set_private' in actions:
            del actions['files_set_private']
        return actions


admin.site.unregister(Page)
admin.site.register(Page, CustomPageAdmin)

admin.site.unregister(RichTextPage)
# CMS-1126
# admin.site.register(RichTextPage, CustomPageAdmin)

admin.site.unregister(WidgyPage)
admin.site.register(WidgyPage, CustomWidgyPageAdmin)

admin.site.unregister(Link)
admin.site.register(Link, CustomLinkAdmin)

admin.site.register(PageExtension)

# CMS-1140
admin.site.unregister(Folder)
admin.site.register(Folder, CustomFilerFolderAdmin)
