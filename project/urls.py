from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from solid_i18n.urls import solid_i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.sitemaps import views
from django.views.generic.base import RedirectView, TemplateView

from haystack.views import SearchView

from zinnia.sitemaps import (EntrySitemap, CategorySitemap,
                             AuthorSitemap, TagSitemap)

from apps.common.forms import ModelSearchForm
from apps.common.views import FullHealthCheck, SimpleHealthCheck

from .sitemaps import (GallerySitemap, GalleryCategorySitemap, NewsSitemap,
                       NewsCategorySitemap, RegionSitemap,
                       MezzaninePageSitemap)

from .widgy_site import site as widgy_site

admin.autodiscover()

sitemaps = {
    'pages': MezzaninePageSitemap,
    'blog': EntrySitemap,
    'blog-category': CategorySitemap,
    'blog-author': AuthorSitemap,
    'blog-tag': TagSitemap,
    'gallery': GallerySitemap,
    'gallery-category': GalleryCategorySitemap,
    'news': NewsSitemap,
    'news-category': NewsCategorySitemap,
    'region': RegionSitemap,
}

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = patterns(
    '',
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ('^admin/', include(admin.site.urls)),
)

urlpatterns += solid_i18n_patterns(
    '',
    # django-filer
    url(r'^filer/', include('filer.urls')),
    # Single pages
    url(r'^vr-collections/$',
        TemplateView.as_view(template_name='single_pages/vr_collections.html'),
        name='vr_collections'),
    # Widgy admin
    url(r'^admin/widgy/', include(widgy_site.urls)),
    # Widgy frontend
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),
    # Zinnia
    # TODO: Consider use blog_urls to prevent accessing zinnia default url
    # imports
    url(r'^blog/3d-space/$',
        RedirectView.as_view(pattern_name='gallery_model_list',
                             permanent=True),
        name='wp_gallery_model_list'),
    url(r'^blog/3d-space/(?P<slug>[-\w]+)/$',
        RedirectView.as_view(pattern_name='gallery_model_detail',
                             permanent=True),
        name='wp_gallery_model_detail'),
    url(r'^blog/', include('zinnia.urls', namespace='zinnia')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # Sitemaps & robots.txt
    url(r'^sitemap\.xml$', views.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', views.sitemap,
        {'sitemaps': sitemaps}),
    url(r'^robots\.txt$', include('robots.urls')),
    # Health check
    url(r'^system/health/simple/?$', SimpleHealthCheck.as_view(),
        name='simple-health-check'),
    url(r'^system/health/full/?$', FullHealthCheck.as_view(),
        name='full-health-check'),
    # Gallery
    url(r'^', include('apps.mp_blog.urls')),
    # Haystack
    url(r'^search/$', SearchView(form_class=ModelSearchForm), name='search'),
    # Trade-in value check
    url(r'^', include('apps.misc.urls')),

    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part.
    # Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/index.html"
    # should be used if you want to customize the homepage's template.

    url(_(r'^$'), 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),

    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    (_('^'), include('mezzanine.urls')),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = 'mezzanine.core.views.page_not_found'
handler500 = 'mezzanine.core.views.server_error'
