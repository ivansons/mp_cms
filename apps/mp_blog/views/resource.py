from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from ..models.resource import (IndustryCategory, TypeCategory, TopicCategory,
                               ResourceEntry)
from .mixins import NoCategoryEntryPreviewMixin


class ResourceList(ListView):
    """
    View returning a list of published resource entries.
    """
    paginate_by = 12
    template_name = 'mp_blog/resource/resource_list.html'

    def _get_slugs_from_category_params(self, params):
        # format:
        #   ?param1=c1,c2&param2=c3,c4&...
        return [slug for slug in params.split(',') if slug] or None

    def get_queryset(self):
        qs = ResourceEntry.published.all()

        # multiple filters
        topics = self.request.GET.get('topics') or ''
        types = self.request.GET.get('types') or ''
        industries = self.request.GET.get('industries') or ''
        topics = self._get_slugs_from_category_params(topics)
        types = self._get_slugs_from_category_params(types)
        industries = self._get_slugs_from_category_params(industries)

        if topics:
            qs = qs.filter(topics__slug__in=topics)
        if types:
            qs = qs.filter(types__slug__in=types)
        if industries:
            qs = qs.filter(industries__slug__in=industries)

        return qs

    def get_context_data(self, **kwargs):
        context = super(ResourceList, self).get_context_data(**kwargs)
        object_ids = context['object_list'].values_list('id', flat=True) or []
        objects = ResourceEntry.objects.filter(id__in=object_ids)
        context['object_list'] = objects.filter(featured=False)
        context['featured_object_list'] = objects.filter(featured=True)
        context['industries'] = IndustryCategory.objects.all()
        context['types'] = TypeCategory.objects.all()
        context['topics'] = TopicCategory.objects.all()
        return context


class ResourceDetail(NoCategoryEntryPreviewMixin, DetailView):
    queryset = ResourceEntry.published.on_site
    template_name = 'mp_blog/resource/resource_detail.html'
    permissions_required = ('mp_blog.can_view_all_resources',)
