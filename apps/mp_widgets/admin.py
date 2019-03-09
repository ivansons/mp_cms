from __future__ import absolute_import

from django.contrib import admin

from apps.common.admin import CustomWidgyPageAdmin
from .models import RawPage


admin.site.register(RawPage, CustomWidgyPageAdmin)
