import os
from pathlib import Path
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ADMINS = (
    ('Henry Udeh', 'admin@ghauzi.com'),
)
MANAGERS = ADMINS
SECRET_KEY = 'django-insecure-_k4%&93vq5j3wchpc_5uej$9yc=27!ydhkw7a786@6rteex=3#'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1','localhost:3000']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # third party
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    
    # app
    'account',
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

WSGI_APPLICATION = 'core.wsgi.application'




LANGUAGE_CODE = 'en'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/



REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_TOKEN_CLASSES': (
        'rest_framework_simplejwt.tokens.AccessToken',
    )
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SITE_ID = 1
AUTH_USER_MODEL = 'account.User'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "De-Ghauzi",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "De-Ghauzi",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/img/logo].jpeg",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome to Ghauzi",

    # Copyright on the footer
    "copyright": "De-Ghauzi",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "account.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["account.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "account."},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "account"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"model": "account.User"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": ['auth.group'],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["account", 'transactions'],

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "fundRaise": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["fundRaise.view_fundRaise"]
    #     }]
    # },


    "icons": {
        "auth": "fas fa-users-cog",
        "account.UserAccount": "fas fa-user",
        "auth.Group": "fas fa-users",
        "profile.CompanyProfile": "fas fa-building",
        "profile.PersonalProfile": "far fa-address-card",
        "auction.Auction":"fab fa-product-hunt",
        "auction.AuctionBid":"fas fa-gavel",
        "fundRaise.DonateCash":"fas fa-hand-holding-usd",
        "fundRaise.DonateToSell":"fas fa-people-carry",
        "fundRaise.RaiseFund":"fas fa-bullhorn",
        "fundRaise.DonationPaymentIntent":"fab fa-cc-visa",
        "donateAdmin.DonateCash":"far fa-handshake",
        "donateAdmin.DonateItem":"fas fa-gift",
        "donateAdmin.CashPaymentHistory":"far fa-money-bill-alt",
        "marketPlace.Orders":"fas fa-cart-arrow-down",
        "marketPlace.ShippingAddress":"fas fa-truck",
        "marketPlace.Auction" :"fas fa-gavel",
        "marketPlace.CashPaymentHistory" :"fab fa-amazon-pay",
        "project.Project":"fas fa-bullhorn",
        "project.ProjectDonation":"fas fa-hand-holding-usd",
        "project.ProjectPaymentIntent":"fab fa-cc-mastercard",
        "customers.client":"fas fa-code-branch",
        "django.sites":"fab fa-chrome"
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"account.UserAcount": "collapsible", "account.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": True,
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}