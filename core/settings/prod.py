'''Use this for production'''

from .base import *
import dj_database_url


DATABASES = {'default': dj_database_url.config('DATABASE_URL')}
# database for django tenants
ALLOWED_HOSTS += ["portal.deghauzimicrolending.com","dashboard.deghauzimicrolending.com "]
WSGI_APPLICATION = 'core.wsgi.prod.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

CORS_ORIGIN_WHITELIST = (
    'http://dashboard.deghauzimicrolending.com',
    'http://portal.deghauzimicrolending.com',
    'http://localhost:3000'
)
CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.com$",
    r"^http://\w+\.com$",
    r"^http://\w+\:3000$",
]
CORS_ORIGIN_ALLOW_ALL = True
STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR,'statifiles')
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = BASE_DIR, 'mediafiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#enforce https
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True