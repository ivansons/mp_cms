import json

from django.http import Http404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView

from django.utils.translation import ugettext_lazy as _

from tagging.models import Tag, TaggedItem
from tagging.utils import get_tag

from ..models.matterapps import MatterAppsEntry as MatterApps
from .mixins import EntryPreviewMixin, EntrySearchMixin

class TagList(ListView):
    """
    This view return a list of all published tags.
    """
    template_name = ''
    context_object_name = 'tag_list'

    def get_queryset(self):
        """
        Return a queryset of published tags,
        with a count of their entries published.
        """
        return Tag.objects.usage_for_queryset(
            MatterApps.published.all(), counts=True)


class AppsList(ListView):
    """
    This view returning a list of published models.
    """
    paginate_by = 20
    template_name = 'mp_blog/matterapps/apps_list.html'

    featured = False

    def get_queryset(self):
        """
        #Return a queryset of all published models.
        """
        qs = MatterApps.objects.filter(status=2)
        if self.featured:
            qs = qs.filter(featured=True)
        if self.kwargs.get('author'):
            # TODO: Switch to JsonField when upgrading Django to 1.9.
            qs = qs.filter(_model_info__icontains='"contact_name":{}'.format(
                json.dumps(self.kwargs['author'])
            ))
        return qs

    def get_context_data(self, **kwargs):
        context = super(AppsList, self).get_context_data(**kwargs)
        context.update({
            'featured': self.featured,
        })
        return context


class AppsSearch(EntrySearchMixin, AppsList):
    """
    View returning a list of published models based on search pattern
    """
    model_cls = MatterApps
    paginate_by = 15
    template_name = 'mp_blog/matterapps/apps_list.html'


class AppsDetail(DetailView):
    """
    Detailed view for an MatterApps.
    """
    model = MatterApps
    template_name = 'mp_blog/matterapps/apps_detail.html'
    permissions_required = [
        'mp_blog.can_view_all_models'
    ]

    def get_context_data(self, **kwargs):
        context = super(AppsDetail, self).get_context_data(**kwargs)

        return context