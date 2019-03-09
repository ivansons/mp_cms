from django.contrib import admin

from zinnia.models import Category, Entry
from zinnia.settings import ENTRY_BASE_MODEL

from ..models.gallery import ModelCategory, ModelEntry
from ..models.news import NewsCategory, NewsEntry
from ..models.resource import (IndustryCategory, TypeCategory, TopicCategory,
                               ResourceEntry)
from ..models.casestudy import CaseStudyEntry
from ..models.region import RegionEntry
from ..models.matterapps import MatterAppsEntry

from .blog import CustomEntryAdmin, EntryCategoryAdmin
from .gallery import ModelEntryAdmin
from .news import NewsEntryCKEditorAdmin
from .resource import ResourceEntryCKEditorAdmin
from .casestudy import CaseStudyEntryCKEditorAdmin
from .region import RegionEntryCKEditorAdmin
from .matterapps import MatterAppsEntryAdmin


admin.site.unregister(Category)
admin.site.register(Category, EntryCategoryAdmin)

if ENTRY_BASE_MODEL == 'zinnia.models_bases.entry.AbstractEntry':
    admin.site.unregister(Entry)
admin.site.register(Entry, CustomEntryAdmin)

admin.site.register(ModelCategory)
admin.site.register(ModelEntry, ModelEntryAdmin)

admin.site.register(NewsCategory)
admin.site.register(NewsEntry, NewsEntryCKEditorAdmin)

admin.site.register(TopicCategory)
admin.site.register(TypeCategory)
admin.site.register(IndustryCategory)
admin.site.register(ResourceEntry, ResourceEntryCKEditorAdmin)
admin.site.register(CaseStudyEntry, CaseStudyEntryCKEditorAdmin)
admin.site.register(RegionEntry, RegionEntryCKEditorAdmin)
admin.site.register(MatterAppsEntry, MatterAppsEntryAdmin)
