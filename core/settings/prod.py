'''Use this for production'''

from .base import *
import dj_database_url


# database
DATABASES = {'default': dj_database_url.config('DATABASE_URL')}
ALLOWED_HOSTS += ["microlending-app-fe.vercel.app", "app-deghauzi.herokuapp.com"]
WSGI_APPLICATION = 'core.wsgi.prod.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'https://microlending-app-fe.vercel.app',
    'https://app-deghauzi.herokuapp.com',
)
CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.com$",
    r"^https://\w+\.vercel.app$",
    r"^https://\w+\.herokuapp.com$",
    r"^http://\w+\.com$",
    r"^http://\w+\:3000$",
]
CORS_ORIGIN_ALLOW_ALL = False
# enforce https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
