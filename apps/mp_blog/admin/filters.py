from zinnia.admin.filters import CategoryListFilter

from ..models.gallery import ModelCategory
from ..models.news import NewsCategory
from ..models.resource import TopicCategory, TypeCategory, IndustryCategory


class ModelCategoryListFilter(CategoryListFilter):
    """
    List filter for ModelEntryAdmin about model categories
    with published entries.
    """
    model = ModelCategory


class NewsCategoryListFilter(CategoryListFilter):
    """
    List filter for NewsEntryAdmin about news categories
    with published entries.
    """
    model = NewsCategory


class ResourceTopicListFilter(CategoryListFilter):
    model = TopicCategory


class ResourceTypeListFilter(CategoryListFilter):
    model = TypeCategory


class ResourceIndustryListFilter(CategoryListFilter):
    model = IndustryCategory
