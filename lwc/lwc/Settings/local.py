__author__ = 'taiowawaner'

"""
Django settings for lwc project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# folder under lwc (lwc)

FOLDER_DIR = (os.path.dirname(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k0l@w9(j)x$ny@!fbft$!5y192cd#^9v6k6amc62y$hzr5z#2^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'joins',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lwc.middleware.ReferMiddleWare',
)

ROOT_URLCONF = 'lwc.urls'

WSGI_APPLICATION = 'lwc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SHARE_URL = "http://launchwithcode.com/?ref="

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# TEMPLATE_CONTEXT_PROCESSORS = (
#     'django.core.context_processors.static',
#     'django.contrib.auth.context_processors.auth',
# )
#
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

STATIC_URL = '/static/'

#/Users/taiowawaner/Documents/Coding_for_Entrepreneurs/coding_for/lwc/static/static_root
#/Users/taiowawaner/Documents/Coding_for_Entrepreneurs/coding_for/lwc/static/static_root
STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'static_root')

#/Users/taiowawaner/Documents/Coding_for_Entrepreneurs/coding_for/lwc/static/static_dirs
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'static_dirs'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

MEDIA_URL = '/media/'


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
