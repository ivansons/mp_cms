"""Settings of MP_BLOG"""
from django.conf import settings

SCANMODEL_API_URL_FORMAT = getattr(
    settings,
    'MP_BLOG_SCANMODEL_API_URL_FORMAT',
    'https://my.matterport.com/api/v1/scanmodel/{}'
)

MODEL_VR_URL_FORMAT = getattr(
    settings,
    'MODEL_VR_URL_FORMAT',
    'https://my.matterport.com/vr/show/?m={}'
)
