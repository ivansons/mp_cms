from ._base import *

ALLOWED_HOSTS = (
    '192.168.140.140',
    # please add entry in /etc/hosts in order to bypass CORS
    'localdev.matterport.com',
)

DEBUG = True

SECRET_KEY = 'av+ogj*+!!(r221q4b8ftb3=3x%7avy5c6l8ut76w5xiletem5'
NEVERCACHE_KEY = '8jz+w-4b)z09b!866uv^^tc8gk_&$x&(hr+o_7s2ya#&&ai5oi'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mp_cms',
        'USER': 'mp_cms',
        'PASSWORD': 'matterport',
        'HOST': '',
        'PORT': '',
    }
}

# no caches in development environment
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# not caching templates in development environment
TEMPLATES = ({
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': (os.path.join(PROJECT_ROOT, 'templates'),),
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.debug',
            'django.core.context_processors.static',
            'django.core.context_processors.media',
            'django.core.context_processors.request',
            'mezzanine.conf.context_processors.settings',
            'mezzanine.pages.context_processors.page',
            'zinnia.context_processors.version',  # Optional
            'apps.common.context_processors.build_number',
        ),
        'loaders': (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
    },
},)

REDIS_CONFIG = {
    'host': '127.0.0.1',
    'port': '6379',
    'protocol': 'redis',
    'password': '',
}

HAYSTACK_CONNECTIONS['default']['PATH'] = 'redis://127.0.0.1:6379/1'

####################
# STORAGE SETTINGS #
####################
AWS_ACCESS_KEY_ID = 'AKIAJO3XXO6YTIOLWDTA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'dev-mp-cms'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


####################
#     Logging      #
####################
LOGS_PATH = os.path.join(PROJECT_ROOT, 'logs/')

if not os.path.exists(LOGS_PATH):
    os.makedirs(LOGS_PATH)

RAVEN_CONFIG = {
    'dsn': 'https://2fce413f67774c28a136fe95581d5bf4:54b36cec27a0407f867f081768eb729d@app.getsentry.com/85838',
}

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
            'filename': os.path.join(LOGS_PATH, 'project.log'),
            'maxBytes': 1024 * 1024 * 25,  # 25 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        # https://django-statsd.readthedocs.org/en/latest/#logging-errors
        'test_statsd_handler': {
            'class': 'django_statsd.loggers.errors.StatsdHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propogate': False,
        },
        'logtool': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': False,
        },
    }
}


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
