"""
Django settings for test_docker1 project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from os import getenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@_3o@uz_c%+@ax##=_m*#xp=^-ca$4=j@9fy%xa7tmqvl3ov0a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'drf_yasg',# para el swagger
    'base',
    'productos',
    'persona_app'
]

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none' #list, full
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_docker1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'test_docker1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'my_database',
    #     'USER': 'root',
    #     'PASSWORD': 'secret',
    #     'HOST': 'mysql',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
    #     }
    # }
    # 'default': {
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': getenv('MYSQL_DATABASE', 'my_database'),
    #     'USER': getenv('MYSQL_USER', 'root'),
    #     'PASSWORD': getenv('MYSQL_PASSWORD', 'secret'),
    #     'HOST': getenv('MYSQL_HOST', 'mysql'),# Use 'mysql' as you defined in your docker-compose.yml
    #     'PORT': getenv('MYSQL_PORT', '3306'),
    #     # 'OPTIONS': {
    #     #     'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     #     'auth_plugin': 'mysql_native_password'
    #     # }
    # }
    # 'default': {
    #     "ENGINE": "django.db.backends.postgresql",
    #     #"ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "postgres",
    #     "USER": "postgres",
    #     "PASSWORD": "postgres",
    #     "HOST": "db",  # set in docker-compose.yml
    #     "PORT": 5432,  # default postgres port
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': getenv('POSTGRES_DB', 'my_database'),
    #     'USER': getenv('POSTGRES_USER', 'postgres'),
    #     'PASSWORD': getenv('POSTGRES_PASSWORD', 'secret'),
    #     'HOST': getenv('POSTGRES_HOST', 'postgres'),# Use 'postgres' as you defined in your docker-compose.yml
    #     'PORT': getenv('POSTGRES_PORT', '5432'),
    #     'OPTIONS': {}
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://ip172-18-0-11-cm5ko1io7r5g009oal20-5173.direct.labs.play-with-docker.com"
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
