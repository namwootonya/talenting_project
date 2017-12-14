"""
Django settings for pratice project.
Generated by 'django-admin startproject' using Django 1.11.6.
For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# Config Paths
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEV_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_dev.json')
CONFIG_SECRET_LOCAL_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_local.json')
config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())
config_secret_local = json.loads(open(CONFIG_SECRET_LOCAL_FILE).read())
# Secret_key
SECRET_KEY = config_secret_common['django']['secret_key']

# Static Path
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')

# Media Paths
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
MEDIA_URL = '/media/'

DEBUG = True

ALLOWED_HOSTS = [
    '.elasticbeanstalk.com',
    'localhost',
    '127.0.0.1',
    '.yabi.kr',
]

# Application definition
INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'storages',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',

    'member',
    'hosting',
    'event',
    'corsheaders',
    'drf_fcm',

]
DRF_FCM = {
    'API_KEY': "AIzaSyACNPFjv3ehXYrz_YAetDUassGsaptv9E4"
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'localhost:3001',
    'front.localhost:8013',
    '.elasticbeanstalk.com',
    'talenting-env.ap-northeast-2.elasticbeanstalk.com',
)

ROOT_URLCONF = 'config.urls'

# DJANGO-REST-FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'utils.exception.handler.custom_exception_handler',
}

# Template
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATES_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'

# Custom User
AUTH_USER_MODEL = 'member.User'
EVENT_ITEM_MODEL = 'event.Event'

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

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'talenting2@gmail.com'
EMAIL_HOST_PASSWORD = 'xkffpsxldqordpsem'
EMAIL_PORT = 587

# Internationalization
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# jet 설정
JET_SIDE_MENU_COMPACT = True
