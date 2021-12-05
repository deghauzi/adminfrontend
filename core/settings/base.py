import os
from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings
from django.utils.translation import gettext_lazy as _
from decouple import config


BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

ADMINS = (
    ('Henry Udeh', 'admin@ghauzi.com'),
)
MANAGERS = ADMINS
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party
    'djoser',
    'social_django',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'cloudinary',

    # app
    'account',
    "withdrawal",
    'contributions',
    'userprofile'
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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


LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DATETIME_FORMAT': "%d/%m/%Y %H:%M:%S",
}

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend'
)

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SET_USERNAME_RETYPE': True,
    'SET_PASSWORD_RETYPE': True,
    'HIDE_USERS': True,
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SOCIAL_AUTH_TOKEN_STRATEGY': 'djoser.social.token.jwt.TokenStrategy',
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': ['http://localhost:3000/google',"https://ogadonate.com/linkedin",
                                          "https://ogadonate.com/twitter", 'https://ogadonate.com/facebook'],
    'SERIALIZERS': {
        'user_create': 'userprofile.auth_serializers.UserCreateSerializer',
        'user': 'djoser.serializers.UserSerializer',
        'current_user': 'djoser.serializers.UserSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    },
    'EMAIL': {
        'activation': 'utils.emailutils.ActivationEmail',
        'confirmation': 'utils.emailutils.ConfirmationEmail',
        'password_reset': 'utils.emailutils.PasswordResetEmail',
        'password_changed_confirmation': 'utils.emailutils.PasswordChangedConfirmationEmail',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1
AUTH_USER_MODEL = 'userprofile.User'
SOCIAL_AUTH_JSONFIELD_ENABLED = True

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
VALID_IMAGE_EXTENSIONS = [
    "jpg",
    "jpeg",
    "png",
]


LOGIN_URL = '/api/auth/jwt/create/'
LOGOUT_URL = '/api/auth/logout'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('SMTP_SERVER', default='')
EMAIL_PORT = config('SMTP_PORT', default=25, cast=int)
EMAIL_HOST_USER = config('SMTP_LOGIN', default='')
EMAIL_HOST_PASSWORD = config('SMTP_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
DEFAULT_FROM_EMAIL = 'De-Ghauzi <noreply@deghauzimicrolending.com>'


# PAYSTACK PAYMENT
# PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY', default='')
# PAYSTACK_SECRET_KEY = config('PAYSTACK_SECRET_KEY', default='')
# PAYSTACK_IP = config('PAYSTACK_IP', default='')


# # Stripe Payment
# STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = config('COMPRESS_ENABLED', False)


