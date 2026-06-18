from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------
# Core
# -----------------------------------------------------------------
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '_^)vd6-d2pd@-vm-e*%ur=apsqz_@8m65#55)#g1t5+$uo9h49')

DEBUG = False  # Always False unless local_settings overrides it

ALLOWED_HOSTS = ['ashemran.shop', 'www.ashemran.shop', 'localhost', '127.0.0.1', 'backend.ashemran.shop', 'www.backend.ashemran.shop']

CSRF_TRUSTED_ORIGINS = ['https://ashemran.shop', 'https://www.ashemran.shop', 'https://backend.ashemran.shop', 'https://www.backend.ashemran.shop']

# -----------------------------------------------------------------
# Applications
# -----------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'rest_framework',
    'corsheaders',
    'ckeditor',
    'blog',
    'home',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'

# -----------------------------------------------------------------
# Database
# -----------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------
# Password validation
# -----------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------------
# Internationalisation
# -----------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
APPEND_SLASH = True

# -----------------------------------------------------------------
# Static & Media files
# -----------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
}
# STORAGES = {
#     'staticfiles': {
#         'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
#     },
#     'default': {
#         'BACKEND': 'django.core.files.storage.FileSystemStorage',
#     },
# }

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -----------------------------------------------------------------
# CKEditor
# -----------------------------------------------------------------
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': '100%',
        'toolbar_Full': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'StrikeThrough', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Source'],
            ['Maximize'],
        ],
    },
}

# -----------------------------------------------------------------
# Django REST Framework
# -----------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# -----------------------------------------------------------------
# CORS
# -----------------------------------------------------------------
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'https://ashemran.shop',
    'https://www.ashemran.shop',
]
CORS_ALLOW_CREDENTIALS = False

# -----------------------------------------------------------------
# Local development overrides (file not present on cPanel server)
# -----------------------------------------------------------------
try:
    from .local_settings import *
except ImportError:
    pass

# -----------------------------------------------------------------
# Security — evaluated last so DEBUG value is final
# -----------------------------------------------------------------
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG
