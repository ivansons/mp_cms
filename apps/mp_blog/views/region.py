from django.views.generic.detail import DetailView

from ..models.region import RegionEntry
from .mixins import NoCategoryEntryPreviewMixin


class RegionDetail(NoCategoryEntryPreviewMixin, DetailView):
    queryset = RegionEntry.published.on_site
    template_name = 'mp_blog/region/region_detail.html'
    permissions_required = ('mp_blog.can_view_all_regions',)
