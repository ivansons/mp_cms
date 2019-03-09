# -*- coding: utf8 -*-
"""
mp_widgets search indexes
"""
from haystack import indexes
from widgy.templatetags.widgy_tags import render_root
from widgy.utils import html_to_plaintext
from widgy.signals import widgy_pre_index

from .models.page import RawPage
from apps.common.utils import prepare_attribute_list


class RawPageIndex(indexes.SearchIndex, indexes.Indexable):
    """
    RawPage (WordPressLayout / NoHeaderFooterLayout) Search Index
    - based on widgy.contrib.widgy_mezzanine.search_indexes.py

    """
    title = indexes.CharField(model_attr='title')
    date = indexes.DateTimeField(model_attr='publish_date')
    description = indexes.CharField(model_attr='description')
    keywords = indexes.MultiValueField()
    get_absolute_url = indexes.CharField(model_attr='get_absolute_url')
    text = indexes.CharField(document=True)

    def full_prepare(self, *args, **kwargs):
        widgy_pre_index.send(sender=self)
        return super(RawPageIndex, self).full_prepare(*args, **kwargs)

    def get_model(self):
        return RawPage

    def index_queryset(self, using=None):
        return self.get_model().objects.published()

    def prepare_text(self, obj):
        context = {'_current_page': obj.page_ptr, 'page': obj.page_ptr}
        html = render_root(context, obj, 'root_node')
        content = html_to_plaintext(html)
        keywords = ' '.join(prepare_attribute_list(obj, 'keywords'))
        return ' '.join([obj.title, keywords, obj.description,
                         content])
