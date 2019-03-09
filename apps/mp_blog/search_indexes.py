# -*- coding: utf8 -*-
"""
mp_blog search indexes
"""
from django.dispatch import Signal
from django.utils.encoding import force_text

from haystack import indexes
from widgy.utils import html_to_plaintext
from zinnia.models import Entry as BlogEntry
from zinnia.managers import PUBLISHED

from .models.gallery import ModelEntry
from .models.news import NewsEntry
from apps.common.utils import prepare_attribute_list

model_entry_pre_index = Signal()
news_entry_pre_index = Signal()
blog_entry_pre_index = Signal()


class BaseSearchIndex(indexes.SearchIndex):
    """
    Base search index class for Gallery, News, Blog

    """
    model = None

    date = indexes.DateTimeField(model_attr='last_update')
    title = indexes.CharField(model_attr='title')
    slug = indexes.CharField(model_attr='slug')
    content = indexes.CharField(model_attr='content')
    image_caption = indexes.CharField(model_attr='image_caption')
    categories = indexes.MultiValueField()
    authors = indexes.MultiValueField()
    tags = indexes.MultiValueField()
    text = indexes.CharField(document=True)

    def get_model(self):
        return self.model

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(status=PUBLISHED)

    def prepare_text(self, obj):
        content = html_to_plaintext(obj.content)
        categories = ' '.join(prepare_attribute_list(obj, 'categories'))
        authors = ' '.join(prepare_attribute_list(obj, 'authors'))
        tags = ' '.join([force_text(k) for k in obj.tags_list])
        return ' '.join([obj.title, content, categories, authors, tags,
                         obj.slug, obj.image_caption])


class ModelEntryIndex(BaseSearchIndex, indexes.Indexable):
    """
    ModelEntry Search Index

    """
    model_subtitle = indexes.CharField(model_attr='model_subtitle')

    def full_prepare(self, *args, **kwargs):
        model_entry_pre_index.send(sender=self)
        return super(ModelEntryIndex, self).full_prepare(*args, **kwargs)

    def get_model(self):
        return ModelEntry

    def prepare_text(self, obj):
        content = html_to_plaintext(obj.content)
        categories = ' '.join(prepare_attribute_list(obj, 'categories'))
        authors = ' '.join(prepare_attribute_list(obj, 'authors'))
        tags = ' '.join([force_text(k) for k in obj.tags_list])
        return ' '.join([obj.title, content, categories, authors, tags,
                         obj.slug, obj.image_caption, obj.model_subtitle])


class NewsEntryIndex(BaseSearchIndex, indexes.Indexable):
    """
    NewsEntry Search Index

    """
    def full_prepare(self, *args, **kwargs):
        news_entry_pre_index.send(sender=self)
        return super(NewsEntryIndex, self).full_prepare(*args, **kwargs)

    def get_model(self):
        return NewsEntry


class BlogEntryIndex(BaseSearchIndex, indexes.Indexable):
    """
    BlogEntry Search Index

    """
    def full_prepare(self, *args, **kwargs):
        blog_entry_pre_index.send(sender=self)
        return super(BlogEntryIndex, self).full_prepare(*args, **kwargs)

    def get_model(self):
        return BlogEntry
