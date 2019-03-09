from django import forms
from django.conf import settings
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.utils.translation import ugettext_lazy as _

from zinnia.admin.forms import EntryAdminForm as _EntryAdminForm
from zinnia.admin.widgets import MiniTextarea
from zinnia.admin.widgets import TagAutoComplete, MPTTFilteredSelectMultiple
from zinnia.admin.fields import MPTTModelMultipleChoiceField

from ..models.gallery import ModelCategory, ModelEntry
from ..models.news import NewsCategory, NewsEntry
from ..models.resource import (TopicCategory, TypeCategory, IndustryCategory,
                               ResourceEntry)
from ..models.casestudy import CaseStudyEntry
from ..models.region import RegionEntry
from ..models.matterapps import MatterAppsEntry
from .editor import CKEditor

CONFIG_NAME = 'zinnia-content'
CKEDITOR_CONFIG = getattr(settings, 'CKEDITOR_CONFIGS', {})
if CONFIG_NAME not in CKEDITOR_CONFIG:
    CONFIG_NAME = 'default'


class EntryAdminForm(_EntryAdminForm):
    """
    Define the CKEditor widget for the content field.
    """
    content = forms.CharField(
        label=_('Content'), required=False,
        widget=CKEditor(config_name=CONFIG_NAME))


class ModelEntryAdminForm(_EntryAdminForm):
    """
    Form for ModelEntry's Admin
    """
    categories = MPTTModelMultipleChoiceField(
        label=_('Categories'), required=False,
        queryset=ModelCategory.objects.all(),
        widget=MPTTFilteredSelectMultiple(_('categories')))
    content = forms.CharField(
        label=_('Content'), required=False,
        widget=CKEditor(config_name=CONFIG_NAME))

    class Meta:
        """
        EntryAdminForm's Meta.
        """
        model = ModelEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'image_caption': MiniTextarea,
        }

    def __init__(self, *args, **kwargs):
        super(ModelEntryAdminForm, self).__init__(*args, **kwargs)
        self.fields['categories'].widget = RelatedFieldWidgetWrapper(
            self.fields['categories'].widget,
            ModelEntry.categories.field.rel,
            self.admin_site)


class NewsEntryAdminForm(_EntryAdminForm):
    categories = MPTTModelMultipleChoiceField(
        label=_('Categories'), required=False,
        queryset=NewsCategory.objects.all(),
        widget=MPTTFilteredSelectMultiple(_('categories')))

    class Meta:
        model = NewsEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'image_caption': MiniTextarea,
        }

    def __init__(self, *args, **kwargs):
        super(NewsEntryAdminForm, self).__init__(*args, **kwargs)
        self.fields['categories'].widget = RelatedFieldWidgetWrapper(
            self.fields['categories'].widget,
            NewsEntry.categories.field.rel,
            self.admin_site)


class ResourceEntryAdminForm(_EntryAdminForm):
    topics = MPTTModelMultipleChoiceField(
        label=_('Topics'), required=False,
        queryset=TopicCategory.objects.all(),
        widget=MPTTFilteredSelectMultiple(_('topics')))
    types = MPTTModelMultipleChoiceField(
        label=_('Types'), required=False,
        queryset=TypeCategory.objects.all(),
        widget=MPTTFilteredSelectMultiple(_('types')))
    industries = MPTTModelMultipleChoiceField(
        label=_('Industries'), required=False,
        queryset=IndustryCategory.objects.all(),
        widget=MPTTFilteredSelectMultiple(_('industries')))

    class Meta:
        model = ResourceEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'image_caption': MiniTextarea,
        }

    def __init__(self, *args, **kwargs):
        super(ResourceEntryAdminForm, self).__init__(*args, **kwargs)
        self.fields['topics'].widget = RelatedFieldWidgetWrapper(
            self.fields['topics'].widget,
            ResourceEntry.topics.field.rel,
            self.admin_site)
        self.fields['types'].widget = RelatedFieldWidgetWrapper(
            self.fields['types'].widget,
            ResourceEntry.types.field.rel,
            self.admin_site)
        self.fields['industries'].widget = RelatedFieldWidgetWrapper(
            self.fields['industries'].widget,
            ResourceEntry.industries.field.rel,
            self.admin_site)


class CaseStudyEntryAdminForm(_EntryAdminForm):
    class Meta:
        model = CaseStudyEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'image_caption': MiniTextarea,
        }


class RegionEntryAdminForm(_EntryAdminForm):
    class Meta:
        model = RegionEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'tags': TagAutoComplete,
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
            'head_content': MiniTextarea,
        }


class MatterAppsAdminForm(_EntryAdminForm):
    class Meta:
        model = MatterAppsEntry
        fields = forms.ALL_FIELDS
        widgets = {
            'price': forms.NumberInput(attrs={}),
            'description': CKEditor(config_name=CONFIG_NAME),
            'lead': MiniTextarea,
            'excerpt': MiniTextarea,
        }
