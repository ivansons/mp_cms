from ._base import *
from ._version import MP_CMS_VERSION
import local
from .local import (
    ALLOWED_HOSTS,
    SECRET_KEY,
    NEVERCACHE_KEY,
    DATABASES,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME,
    AWS_LOCATION,
    AWS_S3_CUSTOM_DOMAIN,
    AWS_S3_URL_PROTOCOL,
    RAVEN_CONFIG,
    LOGS_PATH,
    REDIS_CONFIG,
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_HOST_USER,
    EMAIL_HOST_PASSWORD,
)

DEBUG = False


####################
# STORAGE SETTINGS #
####################
STATIC_URL = 'https://static.matterport.com/mp_cms/{}/'.format(MP_CMS_VERSION)

AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# django-compressor
def get_site():
    from project.widgy_site import site
    return site

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL
COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_CONTEXT = {'site': get_site}


####################
#     Logging      #
####################
LOGS_PATH = os.environ.get('DJANGO_LOGS_PATH') or LOGS_PATH

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': u'%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_PATH, 'mp_cms.log'),
            'maxBytes': 1024 * 1024 * 25,  # 25 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        # https://django-statsd.readthedocs.org/en/latest/#logging-errors
        'test_statsd_handler': {
            'class': 'django_statsd.loggers.errors.StatsdHandler',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': RAVEN_CONFIG['dsn'],
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'sentry'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '{}://{}:{}/{}'.format(
            REDIS_CONFIG['protocol'],
            REDIS_CONFIG['host'],
            REDIS_CONFIG['port'],
            REDIS_DATABASES['caches']['default'],
        ),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
        }
    }
}

HAYSTACK_CONNECTIONS['default']['PATH'] = '{}://{}:{}/{}'.format(
    REDIS_CONFIG['protocol'],
    REDIS_CONFIG['host'],
    REDIS_CONFIG['port'],
    REDIS_DATABASES['whoosh']['db'],
)

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

DEFAULT_FROM_EMAIL = 'noreply@matterport.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
