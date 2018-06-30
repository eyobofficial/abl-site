"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qorv8*ojk^z68i*nmn&k$rpnrboh2x)_m%5*^ekmmp)*cef8_n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs.apps.BlogsConfig',
    'pages.apps.PagesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Addis_Ababa'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'blogs.CustomUser'

LOGOUT_REDIRECT_URL = '/'

# Django-suit Configurations
SUIT_CONFIG = {
    'ADMIN_NAME': 'ABL Electrical Engineering',
    'HEADER_DATE_FORMAT': 'M d, Y',
    'SEARCH_URL': '/admin/pages/brand/',
    'MENU': (
        # Rename app and set icon
        {'app': 'blogs', 'label': 'Blog', 'icon': 'icon-pencil', 'models': (
            {'model': 'blogs.author', 'label': 'Authors'},
            {'model': 'pages.catagory', 'label': 'Blog Catagories'},
            {'model': 'pages.tag', 'label': 'Tags'},
            {'model': 'pages.post', 'label': 'Blog Posts'},
            {'model': 'pages.comment', 'label': 'Comments'},
        )},
        {'app': 'pages', 'label': 'Settings', 'icon': 'icon-cog', 'models': (
            {'model': 'pages.brand', 'label': 'Company Details'},
            {'model': 'pages.slide', 'label': 'Sliding Texts'},
            {'model': 'pages.widget', 'label': 'Home Widgets'},
            {'model': 'pages.staff', 'label': 'Team Staffs'},
            {'model': 'pages.service', 'label': 'Services'},
            {'model': 'pages.testimonial', 'label': 'Testimonials'},
            {'model': 'pages.client', 'label': 'Clients'},
            {'model': 'pages.subscriber', 'label': 'Email Subscribers'},
        )},
        {'label': 'Accounts', 'icon': 'icon-user', 'models': (
            'pages.customuser', 'auth.group',
        )},

    ),
}
