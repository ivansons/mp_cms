# -*- coding: utf8 -*-
"""
Context in project scope
"""

from django.conf import settings


def build_number(request=None):
    """
    Add build_number context variable.

    `build_number` is generated in build process.
    """
    return {
        'build_number': getattr(settings, 'MP_CMS_VERSION', ''),
    }
