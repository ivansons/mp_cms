from django.template import Library

from apps.mp_blog.models.region import RegionEntry

register = Library()


@register.inclusion_tag('_footer_region.html')
def region_in_footer():
    return {'regions': RegionEntry.published.filter(
        in_footer=True).order_by('region')}
