# -*- coding: utf8 -*-
"""
Matterport-specific middleware
"""
from __future__ import unicode_literals

import urlparse

from django.contrib.redirects.models import Redirect
from django.http import HttpResponsePermanentRedirect, HttpResponseGone

from mezzanine.core.middleware import RedirectFallbackMiddleware as \
    BaseRedirectFallbackMiddleware
from mezzanine.pages.middleware import PageMiddleware as BasePageMiddleware
from mezzanine.pages.views import page as page_view
from mezzanine.utils.sites import current_site_id


class PageMiddleware(BasePageMiddleware):
    """
    Mezzanine's built-in PageMiddleware runs query for all of requests to
    determine if there is a valid mezzanine page. This causes some performance
    loss.

    This custom page middleware first check the view function and only works
    if view function is mezzanine's page view function.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Per-request mechanics for the current page object.
        """
        if view_func == page_view:
            response = super(PageMiddleware, self).process_view(
                request, view_func, view_args, view_kwargs)
            if response and hasattr(request, 'page') \
                    and request.page.content_model == 'rawpage':
                page = request.page.get_content_model()
                response['Content-Type'] = '%s; charset=%s' % (
                    page.response_content_type,
                    response.charset)
            return response


class RedirectFallbackMiddleware(BaseRedirectFallbackMiddleware):
    """
    Port of Mezzanine's ``RedirectFallbackMiddleware`` that ignores
    query strings in url.
    """
    def process_response(self, request, response):
        response = super(RedirectFallbackMiddleware, self).process_response(
            request, response)
        if response.status_code == 404:
            old_path = request.get_full_path()
            url_parsed = urlparse.urlparse(old_path)
            if url_parsed.path != old_path:
                try:
                    redirect = Redirect.objects.get(
                        site_id=current_site_id(),
                        old_path=url_parsed.path)
                except Redirect.DoesNotExist:
                    pass
                else:
                    if not redirect.new_path:
                        response = HttpResponseGone()
                    else:
                        response = HttpResponsePermanentRedirect(
                            redirect.new_path)
        return response


class XframeOptionsExemptMiddleware(object):
    """
    Honor `allow_iframe` flag in page extension.
    """
    def process_response(self, request, response):
        if hasattr(request, 'page') and hasattr(request.page, 'extension'):
            allow_iframe = request.page.extension.allow_iframe
            if allow_iframe and 'X-Frame-Options' in response:
                del response['X-Frame-Options']
            elif allow_iframe is False:
                response['X-Frame-Options'] = 'DENY'
        return response
