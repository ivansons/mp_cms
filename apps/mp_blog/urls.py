from __future__ import unicode_literals

from django.conf.urls import url
from django.views.generic import RedirectView
from django.utils.translation import ugettext_lazy as _

from .views.gallery import (ModelDetail, ModelList, ModelSearch,
                            SuggestSpace, TagList)
from .views.news import NewsDetail, NewsList
from .views.resource import ResourceList, ResourceDetail
from .views.casestudy import CaseStudyDetail
from .views.region import RegionDetail
from .views.matterapps import (AppsList, AppsDetail)

urlpatterns = [
    url(_(r'^ecosystem/(?P<slug>[-\w]+)/$'),
        AppsDetail.as_view(),
        name='matterapps_detail'),
    url(_(r'^ecosystem/$'),
        AppsList.as_view(),
        name='matterapps_list'),
    url(_(r'^gallery/search/$'),
        ModelSearch.as_view(),
        name='gallery_model_search'),
    url(_(r'^gallery/suggest-a-space/$'),
        SuggestSpace.as_view(),
        name='gallery_suggest_space'),
    url(_(r'^gallery/$'),
        ModelList.as_view(),
        name='gallery_model_list'),
    url(_(r'^gallery/featured/$'),
        ModelList.as_view(featured=True),
        name='gallery_featured_model'),
    url(_(r'^gallery/vr/$'),
        ModelList.as_view(),
        name='gallery_vr_model'),
    url(_(r'^gallery/category/(?P<slug>[a-zA-Z0-9\-]+)/$'),
        ModelList.as_view(),
        name='gallery_model_in_category'),
    url(_(r'^gallery/tags/$'),
        TagList.as_view(),
        name='gallery_tag_list'),
    url(_(r'^gallery/tags/(?P<tag>[^/]+(?u))/$'),
        ModelList.as_view(),
        name='gallery_model_by_tag'),
    url(_(r'^gallery/user/(?P<creator>[^/]+(?u))/$'),
        ModelList.as_view(),
        name='gallery_model_by_creator'),
    url(_(r'^3d-space/(?P<slug>[-\w]+)/$'),
        ModelDetail.as_view(),
        name='gallery_model_detail'),
    url(_(r'^news/$'),
        NewsList.as_view(category_name='In the News',),
        name='in_the_news_news_list'
        ),
    url(_(r'^news/matterport-press-releases/$'),
        NewsList.as_view(category_name='Press Releases'),
        name='press_releases_news_list'),
    url(_(r'^news/customer-press-releases/$'),
        NewsList.as_view(category_name='Customers'),
        name='customers_news_list'),
    # url(r'^news/press-inquiries/$',
    #     PressInquiriesView.as_view(),
    #     name='press_inquiries'),
    url(_(r'^matterport-news/$'),
        RedirectView.as_view(url='/news/matterport-press-releases',
                             permanent=False)),
    url(_(r'^matterport-news/(?P<slug>[-\w]+)/$'),
        NewsDetail.as_view(),
        name='news_detail'),
    url(_(r'^resources/$'), ResourceList.as_view(), name='resource_list'),
    url(_(r'^resources/(?P<slug>[a-zA-Z0-9\-]+)/$'), ResourceDetail.as_view(),
        name='resource_detail'),
    url(_(r'^case-study/(?P<slug>[a-zA-Z0-9\-]+)/$'), CaseStudyDetail.as_view(),
        name='case_study_detail'),
    url(_(r'^3d-real-estate-photography-services/(?P<slug>[a-zA-Z0-9\-]+)/$'),
        RegionDetail.as_view(), name='region_detail'),
]

from .signals import create_thumbnail_callback
