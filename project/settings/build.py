from ._base import *
from ._version import MP_CMS_VERSION

ALLOWED_HOSTS = ('localhost', '127.0.0.1')

DEBUG = True

SECRET_KEY = 'just for build'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

STATIC_URL = 'https://static.matterport.com/mp_cms/{}/'.format(MP_CMS_VERSION)

# Static files are server externally. The static files introduced by
# django-compressor have been generated before uploading.
COMPRESS_OFFLINE = True


def get_site():
    from project.widgy_site import site
    return site

COMPRESS_OFFLINE_CONTEXT = {'site': get_site}


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
