from django.views.generic.detail import DetailView

from ..models.casestudy import CaseStudyEntry
from .mixins import NoCategoryEntryPreviewMixin


class CaseStudyDetail(NoCategoryEntryPreviewMixin, DetailView):
    queryset = CaseStudyEntry.published.on_site
    template_name = 'mp_blog/case_study/case_study_detail.html'
    permissions_required = ('mp_blog.can_view_all_case_studies',)
