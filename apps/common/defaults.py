"""
Default settings for the `mp_cms`.
The `editable` argument for each controls whether
the setting is editable via Django's admin.
"""
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import register_setting


register_setting(
    name='TEMPLATE_ACCESSIBLE_SETTINGS',
    append=True,
    default=(
        'GOOGLE_GTM_ID',
        'GOOGLE_GTM_ENABLED',
        'TRANSIFEX_API_KEY',
    ),
)

register_setting(
    name='GOOGLE_GTM_ID',
    label=_('Google Tag Manager ID'),
    description=_('Google Tag Manager ID '
                  '(https://www.google.com/analytics/tag-manager/)'),
    editable=True,
    default='',
)

register_setting(
    name='GOOGLE_GTM_ENABLED',
    label=_('Google Tag Manager'),
    description=_('Enable: manage all tags in GTM; disable: use individual tags (tracking code)'),
    editable=True,
    choices=(
        (True, _('Enable')),
        (False, _('Disable')),
    ),
    default=False,
)

register_setting(
    name='GOOGLE_OAUTH2_CLIENT_EMAIL',
    label=_('Google OAuth 2.0 Client Email'),
    editable=True,
    default='',
)

register_setting(
    name='GOOGLE_OAUTH2_PRIVATE_KEY',
    label=_('Google OAuth 2.0 Private Key'),
    editable=True,
    default='',
)

register_setting(
    name='GOOGLE_SPREADSHEET_ID',
    label=_('Google Spreadsheet ID'),
    editable=True,
    default='',
)

register_setting(
    name='TRANSIFEX_API_KEY',
    label=_('Transifex API Key'),
    editable=True,
    default='',
)
