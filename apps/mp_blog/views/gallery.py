import json

from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from tagging.models import Tag, TaggedItem
from tagging.utils import get_tag

from ..models.gallery import ModelCategory, ModelEntry
from .mixins import EntryPreviewMixin, EntrySearchMixin


class TagList(ListView):
    """
    View return a list of all published tags.
    """
    template_name = 'mp_blog/gallery/tag_list.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        """
        Return a queryset of published tags,
        with a count of their entries published.
        """
        return Tag.objects.usage_for_queryset(
            ModelEntry.published.all(), counts=True)


class ModelList(ListView):
    """
    View returning a list of published models.
    """
    paginate_by = 12
    template_name = 'mp_blog/gallery/model_list.html'

    featured = False
    vr = False

    def get_tag(self):
        if self.kwargs.get('tag'):
            tag = get_tag(self.kwargs['tag'])
            if tag is None:
                raise Http404('No Tag found matching "%s".' %
                              self.kwargs['tag'])
            return tag

    def get_queryset(self):
        """
        Return a queryset of published models.
        """
        qs = ModelEntry.published.all()
        if self.featured:
            qs = qs.filter(featured=True)
        if self.vr:
            qs = qs.exclude(model_vr_link='')
        slug = self.kwargs.get('slug')
        if slug:
            qs = qs.filter(categories__slug=slug)
        tag = self.get_tag()
        if tag:
            qs = TaggedItem.objects.get_by_model(qs, tag)
        if self.kwargs.get('creator'):
            # TODO: Switch to JsonField when upgrading Django to 1.9.
            qs = qs.filter(_model_info__icontains='"contact_name":{}'.format(
                json.dumps(self.kwargs['creator'])
            ))
        return qs.select_related(
            'image'
        ).prefetch_related(
            'authors',
            'categories',
        )

    def get_context_data(self, **kwargs):
        context = super(ModelList, self).get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context.update({
            'categories': ModelCategory.objects.all(),
            'category': ModelCategory.objects.filter(slug=slug).first(),
            'featured': self.featured,
            'slug': slug,
            'vr': self.vr,
        })
        return context


class ModelSearch(EntrySearchMixin, ModelList):
    """
    View returning a list of published models based on search pattern
    """
    model_cls = ModelEntry
    paginate_by = 15
    template_name = 'mp_blog/gallery/model_list.html'


class ModelDetail(EntryPreviewMixin, DetailView):
    """
    Detailed view for an ModelEntry.
    """
    queryset = ModelEntry.published.on_site
    template_name = 'mp_blog/gallery/model_detail.html'
    permissions_required = [
        'mp_blog.can_view_all_models'
    ]

    def get_context_data(self, **kwargs):
        context = super(ModelDetail, self).get_context_data(**kwargs)

        category = None
        entries = None

        categories = self.object.categories.all()
        if categories:
            category = categories[0]
            entries = category.entries.all()[:5]

        context['category'] = category
        context['entries'] = entries

        return context


class SuggestSpace(TemplateView):
    """
    Template view for suggest a space.
    """

    template_name = 'mp_blog/gallery/suggest_a_space.html'
