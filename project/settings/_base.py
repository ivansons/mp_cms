from __future__ import absolute_import, unicode_literals
import os

from django.utils.translation import ugettext_lazy as _


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
#
# ADMIN_MENU_ORDER = (
#     ("Content", ("pages.Page", "blog.BlogPost",
#        "generic.ThreadedComment", (_("Media Library"), "fb_browse"),)),
#     ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
#     ("Users", ("auth.User", "auth.Group",)),
# )
ADMIN_MENU_ORDER = (
    ('Widgy', (
        'pages.Page',
        'common.PageExtension',
        'page_builder.Callout',
        'form_builder.Form',
        ('Review queue', 'review_queue.ReviewedVersionCommit'),
        ('File manager', 'filer.Folder'),
    )),
    ('Gallery', (
        ('Model Categories', 'mp_blog.ModelCategory'),
        ('Model Entries', 'mp_blog.ModelEntry'),
    )),
    ('Blog', (
        'mp_blog.CategoryExtension',
        'zinnia.Category',
        'zinnia.Entry',
    )),
    ('News', (
        ('News Categories', 'mp_blog.NewsCategory'),
        ('News Entries', 'mp_blog.NewsEntry'),
    )),
    ('Resource', (
        ('Resource Topics', 'mp_blog.TopicCategory'),
        ('Resource Types', 'mp_blog.TypeCategory'),
        ('Resource Industries', 'mp_blog.IndustryCategory'),
        ('Resource Entries', 'mp_blog.ResourceEntry'),
    )),

    ('Matterapps', (
       ('App Entries', 'mp_blog.MatterAppsEntry'),
    )),

    ('Case Study', (
        ('Case Study Quotes', 'mp_blog.CaseStudyQuote'),
        ('Case Study Entries', 'mp_blog.CaseStudyEntry'),
    )),
    ('Region (Geo)', (
        ('Region Entries', 'mp_blog.RegionEntry'),
    )),
)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
#
# DASHBOARD_TAGS = (
#     ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
#     ("comment_tags.recent_comments",),
#     ("mezzanine_tags.recent_actions",),
# )

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, _('Navigation'), 'pages/menus/navigation.html'),
    # (2, _('Footer'), 'pages/menus/footer.html'),  # footer is hard-coded
    (3, _('Mobile navigation'), 'pages/menus/navigation_mobile.html'),
)

PAGE_MENU_TEMPLATES_DEFAULT = ()

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
# EXTRA_MODEL_FIELDS = (
#     (
#         # Dotted path to field.
#         "mezzanine.blog.models.BlogPost.image",
#         # Dotted path to field class.
#         "somelib.fields.ImageField",
#         # Positional args for field class.
#         (_("Image"),),
#         # Keyword args for field class.
#         {"blank": True, "upload_to": "blog"},
#     ),
#     # Example of adding a field to *all* of Mezzanine's content types:
#     (
#         "mezzanine.pages.models.Page.another_field",
#         "IntegerField", # 'django.db.models.' is implied if path is omitted.
#         (_("Another name"),),
#         {"blank": True, "default": 1},
#     ),
# )

# Setting to turn on featured images for blog posts. Defaults to False.
#
# BLOG_USE_FEATURED_IMAGE = True

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
# USE_MODELTRANSLATION = False


########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

# Supported languages
LANGUAGES = (
    ('en', _('English')),
    ('en-gb', _('English (UK)')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('de', _('German')),
    ('it', _('Italian')),
    ('ja-jp', _('Japanese')),
)

DEBUG = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

AUTHENTICATION_BACKENDS = (
    'mezzanine.core.auth_backends.MezzanineBackend',
)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0644


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public_html/static')

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public_html/media')

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = '{}.urls'.format(PROJECT_APP)

# caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


################
# APPLICATIONS #
################

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = 'filebrowser_safe'
PACKAGE_NAME_GRAPPELLI = 'grappelli_safe'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    # django-haystack search
    'haystack',
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    # 'mezzanine.blog',
    # 'mezzanine.forms',
    # 'mezzanine.galleries',
    # 'mezzanine.twitter',
    # 'mezzanine.accounts',
    # 'mezzanine.mobile',
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
    # django-colorful
    'colorful',
    # django-orderable
    'orderable',
    # Sentry
    'raven.contrib.django.raven_compat',
    # django-storages
    'storages',
    # Widgy apps
    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.review_queue',
    'widgy.contrib.widgy_mezzanine',
    # Widgy dependencies
    'filer',
    'easy_thumbnails',
    'compressor',
    'argonauts',
    'sorl.thumbnail',
    # zinnia
    'mptt',
    'tagging',
    'zinnia',
    'ckeditor',
    'ckeditor_uploader',
    # Widgy requires admin to be installed at the end
    'django.contrib.admin',
    # django-robots
    'robots',
    # django-seo-js (Prerender IO)
    # 'django_seo_js',
    # mp_cms apps
    'apps.common',
    'apps.mp_widgets',
    'apps.mp_blog',
    'apps.misc',
)

ADMIN_MEDIA_PREFIX = '{}grappelli/'.format(STATIC_URL)
TESTING = False
GRAPPELLI_INSTALLED = True
WIDGY_MEZZANINE_SITE = '{}.widgy_site.site'.format(PROJECT_APP)
ZINNIA_ENTRY_BASE_MODEL = 'apps.mp_blog.zinnia_models_bases.BlogAbstractEntry'
ZINNIA_PREVIEW_MAX_WORDS = 20
ZINNIA_PROTOCOL = 'https'

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
            ('django.template.loaders.cached.Loader', (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            )),
        ),
    },
},)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    'django_statsd.middleware.GraphiteRequestTimingMiddleware',
    'django_statsd.middleware.GraphiteMiddleware',
    'mezzanine.core.middleware.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # check `xframe_options_exempt` of a page through page extension
    'apps.common.middleware.XframeOptionsExemptMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'mezzanine.core.request.CurrentRequestMiddleware',
    # replace mezzanine's built-in RedirectFallbackMiddleware to ignore
    # query string
    'apps.common.middleware.RedirectFallbackMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.core.middleware.SitePermissionMiddleware',
    # replace mezzanine's built-in PageMiddleWare for better performance
    'apps.common.middleware.PageMiddleware',
    'mezzanine.core.middleware.FetchFromCacheMiddleware',
    # django_seo_js middleware classes
    #'django_seo_js.middleware.EscapedFragmentMiddleware',  # If you're using #!
    #'django_seo_js.middleware.UserAgentMiddleware',  # If you want to detect by user agent
)

# The STATICFILES_DIRS setting should not contain the STATIC_ROOT setting
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# django-compressor
STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = None
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'apps.common.compressor.DjangoScssFilter'),
)

CKEDITOR_JQUERY_URL = \
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
    # Customization for zinnia content editor if desired
    # 'zinnia-content': {
    #     'toolbar_Zinnia': [
    #         ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
    #         ['Undo', 'Redo'],
    #         ['Scayt'],
    #         ['Link', 'Unlink', 'Anchor'],
    #         ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
    #         ['Source'],
    #         ['Maximize'],
    #         '/',
    #         ['Bold', 'Italic', 'Underline', 'Strike',
    #          'Subscript', 'Superscript', '-', 'RemoveFormat'],
    #         ['NumberedList', 'BulletedList', '-',
    #          'Outdent', 'Indent', '-', 'Blockquote'],
    #         ['Styles', 'Format'],
    #     ],
    #     'toolbar': 'Zinnia',
    # },
}

# Redis DB settings
REDIS_DATABASES = {
    'whoosh': {
        'db': 1,
    },
    'caches': {
        'default': 2,
    }
}

DJANGO_REDIS_LOG_IGNORED_EXCEPTIONS = True

# http://www.agmweb.ca/2011-12-22-django-statsd/
STATSD_CLIENT = 'django_statsd.clients.normal'
STATSD_PREFIX = 'mp_cms'
STATSD_PATCHES = [
    'django_statsd.patches.db',
    'django_statsd.patches.cache',
]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'apps.common.whoosh_redis.RedisEngine',
        'PATH': None,
    },
}
INCLUDE_SPELLING = False

# Real time updates to search index
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.BaseSignalProcessor'

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    'django_extensions',
)

# Migration for Mezzanine field extension
MIGRATION_MODULES = {
    'zinnia': 'apps.mp_blog.zinnia_migrations',
}

# Backend to use
# SEO_JS_BACKEND = "django_seo_js.backends.PrerenderIO"   # PrerenderIO Is default, Don't needed

# Whether to run the middlewares and update_cache_for_url.  Useful to set False for unit testing.
#SEO_JS_ENABLED = True # Defaults to *not* DEBUG.

# If you're using prerender.io (the default backend):
#SEO_JS_PRERENDER_TOKEN = "KNjtTnDlAQVHdqqmyCR0"

# User-agents to render for, if you're using the UserAgentMiddleware
# Defaults to the most popular.  If you have custom needs, pull from the full list:
# http://www.useragentstring.com/pages/Crawlerlist/
"""SEO_JS_USER_AGENTS = [
    "Googlebot",
    "Yahoo",
    "bingbot",
    "Badiu",
    "Ask Jeeves",
]"""

# Urls to skip the rendering backend, and always render in-app.
# Defaults to excluding sitemap.xml.
"""SEO_JS_IGNORE_URLS = [
    "/sitemap.xml",
]
SEO_JS_IGNORE_EXTENSIONS = [
    ".xml",
    ".txt",
    # See helpers.py for full list of extensions ignored by default.
]"""

SOLID_I18N_USE_REDIRECTS = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
