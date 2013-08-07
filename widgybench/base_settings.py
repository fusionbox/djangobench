DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = ':memory:'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

SECRET_KEY = "NOT REALLY SECRET"

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',

    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'django.contrib.comments',
    'django.contrib.sites',
    'filebrowser_safe',
    'grappelli_safe',

    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.urlconf_include',

    'filer',
]

STATIC_URL = '/static/'
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
TESTING = False
GRAPPELLI_INSTALLED = True
SITE_ID = 1

WIDGY_MEZZANINE_SITE = 'widgybench.site'
URLCONF_INCLUDE_CHOICES = []
