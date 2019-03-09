from __future__ import unicode_literals

from django import template

import bleach

register = template.Library()


@register.filter(name='bleach')
def _bleach(html_content):
    """ Remove all HTML tags """
    html_content = html_content if isinstance(html_content, basestring) \
        else str(html_content)
    cleaned_html = bleach.clean(
        html_content or '',
        tags=[],
        attributes={},
        styles=[],
        strip=True
    )
    return ' '.join(cleaned_html.split())
