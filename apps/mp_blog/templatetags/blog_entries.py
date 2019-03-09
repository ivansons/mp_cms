"""Template tags and filters for blog entries"""
from django.template import Library

from zinnia.models.entry import Entry

register = Library()


@register.assignment_tag
def get_top_featured_entries(number=5):
    """
    Return top N featured entries.
    """
    return list(Entry.published.filter(featured=True)[:number])
