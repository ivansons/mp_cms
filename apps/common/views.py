# -*- coding: utf8 -*-
"""
Matterport-specific common app views
"""
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.generic import View

from .forms import FreeGeoIPLogForm


class SimpleHealthCheck(View):
    """
    Startup check: responds with a 200 ok
    """

    def get(self, request):
        try:
            return JsonResponse({'simple_health_check': 'OK'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=503)


class FullHealthCheck(View):
    """
    Startup check: is Database working?
    If something fails, returns a 503 with a {error: 'error description'}
    dictionary. Otherwise returns a 200, with a dict of {key: 'status/warnings
    for each import component'}
    """

    def get(self, request):
        try:
            return JsonResponse({'db': self.check_db()})
        except RuntimeError as e:
            return JsonResponse({'error': str(e)}, status=503)

    def check_db(self):
        try:
            User.objects.all()[0]
        except Exception:
            raise RuntimeError('Failed to get from DB')
        return 'OK'
