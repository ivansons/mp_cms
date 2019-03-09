from __future__ import unicode_literals

from django.conf.urls import url

from .views import check_trade_in_value, google_forms_proxy

urlpatterns = (
    url(r'^api/trade-in-value/$', check_trade_in_value,
        name='check_trade_in_value'),
    url(r'^api/google-forms/$', google_forms_proxy, name='google-forms-proxy'),
)
