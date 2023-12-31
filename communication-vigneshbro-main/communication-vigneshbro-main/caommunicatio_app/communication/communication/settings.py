



import os
import environ
from pathlib import Path
from os.path import dirname, join


env = environ.Env()
environ.Env.read_env()
BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = env('SECRET_KEY')


DEBUG = True
ALLOWED_HOSTS = ["*"]





INSTALLED_APPS = [
                    'django.contrib.admin',
                    'django.contrib.auth',
                    'django.contrib.contenttypes',
                    'django.contrib.sessions',
                    'django.contrib.messages',
                    'django.contrib.staticfiles',
                    #restframework
                    'rest_framework.authtoken',
                    'rest_framework',
                    #custom apps
                    'communicate',
                    'corsheaders',
                    'call'
                ]

MIDDLEWARE = [
                    'django.middleware.security.SecurityMiddleware',
                    'django.contrib.sessions.middleware.SessionMiddleware',
                    'django.middleware.common.CommonMiddleware',
                    'django.middleware.csrf.CsrfViewMiddleware',
                    'django.contrib.auth.middleware.AuthenticationMiddleware',
                    'django.contrib.messages.middleware.MessageMiddleware',
                    'django.middleware.clickjacking.XFrameOptionsMiddleware',
                    'corsheaders.middleware.CorsMiddleware',
            ]

ROOT_URLCONF = 'communication.urls'


REST_FRAMEWORK = {
                    'DEFAULT_AUTHENTICATION_CLASSES': [
                                                            'rest_framework.authentication.BasicAuthentication',
                                                            'rest_framework.authentication.SessionAuthentication',
                                                      ]
                 }



TEMPLATES = [

                {

                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [],
                    'APP_DIRS': True,
                    'OPTIONS':
                                    {
                                        'context_processors':
                                                               [
                                                                    'django.template.context_processors.debug',
                                                                    'django.template.context_processors.request',
                                                                    'django.contrib.auth.context_processors.auth',
                                                                    'django.contrib.messages.context_processors.messages',
                                                                ],
                                    },
                },
            ]

WSGI_APPLICATION = 'communication.wsgi.application'


DATABASES = {
                'default':
                            {
                                'ENGINE': 'django.db.backends.sqlite3',
                                'NAME': BASE_DIR / 'db.sqlite3',
                            }
            }



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


CORS_ALLOWED_ORIGINS = []
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'https://ff63-45-112-138-70.in.ngrok.io/',
]
CORS_ORIGIN_REGEX_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://ff63-45-112-138-70.in.ngrok.io/',
]




USE_TZ = True
USE_I18N = True
USE_L10N = True
EMAIL_PORT = 587
TIME_ZONE = 'UTC'
EMAIL_USE_TLS = True
STATIC_URL = '/static/'
LANGUAGE_CODE = 'en-us'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND ="django.core.mail.backends.smtp.EmailBackend"
