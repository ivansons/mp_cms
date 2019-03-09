from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from mezzanine.pages.models import Page
from zinnia.managers import PUBLISHED
from zinnia.sitemaps import EntryRelatedSitemap
from apps.mp_blog.models.gallery import ModelEntry, ModelCategory
from apps.mp_blog.models.news import NewsEntry
from apps.mp_blog.models.region import RegionEntry


class GallerySitemap(Sitemap):
    """
    Sitemap for gallery model entries
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ModelEntry.objects.filter(status=PUBLISHED)

    def lastmod(self, obj):
        return obj.last_update


class GalleryCategorySitemap(EntryRelatedSitemap):
    """
    Sitemap for gallery model categories.
    """
    model = ModelCategory


class NewsSitemap(Sitemap):
    """
    Sitemap for news entries
    """
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return NewsEntry.objects.filter(status=PUBLISHED)

    def lastmod(self, obj):
        return obj.last_update


class NewsCategorySitemap(Sitemap):
    """
    Sitemap for news categories
    """
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['in_the_news_news_list', 'press_releases_news_list',
                'customers_news_list']

    def location(self, item):
        return reverse(item)


class RegionSitemap(Sitemap):
    """
    Sitemap for region model entries
    """
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return RegionEntry.objects.filter(status=PUBLISHED)

    def lastmod(self, obj):
        return obj.last_update


class MezzaninePageSitemap(Sitemap):
    """
    Sitemap for mezzanine/widgy pages
    """
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return Page.objects.published().filter(in_sitemap=True)

    def lastmod(self, obj):
        return obj.updated
