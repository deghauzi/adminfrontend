'''Use this for development'''

from .base import *


ALLOWED_HOSTS += ['localhost','.localhost','127.0.0.1']
DEBUG  = False

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",  
        "NAME": "memo",
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

STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)