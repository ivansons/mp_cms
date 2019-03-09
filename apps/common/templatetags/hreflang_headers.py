from collections import OrderedDict

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def hreflang_headers(context):
    request = context['request']
    original_path = full_path = request.get_full_path()
    pre_path = '{}://{}'.format(request.scheme, request.get_host())
    languages = []

    for code, _ in settings.LANGUAGES:
        if full_path.startswith('/{}/'.format(code)):
            original_path = full_path[len(code) + 1:]
            break

    for code, _ in settings.LANGUAGES:
        if code == 'en':
            url = '{}{}'.format(pre_path, original_path)
            d = OrderedDict()
            d['rel'] = 'canonical'
            d['href'] = url
            languages.append(d)

            d = OrderedDict()
            d['rel'] = 'alternate'
            d['hreflang'] = 'x-default'
            d['href'] = url
            languages.append(d)

            d = OrderedDict()
            d['rel'] = 'alternate'
            d['hreflang'] = code
            d['href'] = url
            languages.append(d)
        else:
            d = OrderedDict()
            d['rel'] = 'alternate'
            d['hreflang'] = code
            d['href'] = '{}/{}{}'.format(pre_path, code, original_path)
            languages.append(d)

    links = ['<link {}>'.format(' '.join(['{}="{}"'.format(key, value)
                                          for key, value in language.items()]))
             for language in languages]

    return mark_safe('\n'.join(links))
