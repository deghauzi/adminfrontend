'''Use this for development'''

from .base import *


ALLOWED_HOSTS += ['localhost','.localhost','127.0.0.1']
DEBUG  = True

WSGI_APPLICATION = 'core.wsgi.application.dev'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",  
        "NAME": "de_ghauzi",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432", 
    }
}
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    
) 
CORS_ORIGIN_ALLOW_ALL = True

# STATIC_URL = '/staticfiles/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# MEDIA_URL = '/mediafiles/'
# MEDIA_ROOT = BASE_DIR, 'mediafiles'
# STATICFILES_DIRS = ((BASE_DIR /'static'),)
STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR,'statifiles')
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = BASE_DIR, 'mediafiles'
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)