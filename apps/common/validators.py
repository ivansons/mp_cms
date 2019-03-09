# -*- coding: utf8 -*-
"""
Matterport-specific common app validators
"""
from django.core.validators import RegexValidator


class HttpStatusValidator(RegexValidator):
    regex = '^[0-9]{3}$'
    message = 'Please enter a valid HTTP status code, such as 404.'

validate_http_status_code = HttpStatusValidator()


class CountryCodeValidator(RegexValidator):
    regex = '^[A-Z]{2}$'
    message = 'Please enter a valid country code, such as US.'

validate_country_code = CountryCodeValidator()
