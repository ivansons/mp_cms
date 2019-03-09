from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import requests

from .utils import get_trade_in_value


def check_trade_in_value(request):
    serial_number = request.GET.get('serial_number')
    if serial_number:
        value = get_trade_in_value(serial_number)
        if value:
            return JsonResponse({
                'status': 'OK',
                'serial-number': serial_number,
                'value': value,
            })
    return JsonResponse({
        'status': 'ERROR',
        'message': 'Missing or unknown camera serial number'
    }, status=400)


@csrf_exempt
def google_forms_proxy(request):
    """
    POST to public Google Forms.
    """
    data = request.POST.copy()
    url = data.pop('url', None)
    validate_url = URLValidator(schemes=('http', 'https'))
    if url:
        url = url[0]
        try:
            validate_url(url)
            if not url.startswith('https://docs.google.com/forms'):
                raise ValidationError('Invalid Google Forms URL')
        except ValidationError:
            return JsonResponse({
                'status': 'ERROR',
                'message': 'Invalid Google Forms URL',
            }, status=400)

        response = requests.post(url, data=data)
        if response.status_code == 200:
            return JsonResponse({
                'status': 'OK',
            })
    return JsonResponse({
        'status': 'ERROR',
    }, status=400)
