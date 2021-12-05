'''Use this for production'''

from .base import *
import dj_database_url

DEBUG = config('DEBUG',default=False,cast=bool)
DATABASES = {'default': dj_database_url.config('DATABASE_URL')}
# database for django tenants
ALLOWED_HOSTS += ["portal.deghauzimicrolending.com","dashboard.deghauzimicrolending.com"]
WSGI_APPLICATION = 'core.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

CORS_ORIGIN_WHITELIST = (
    'https://dashboard.deghauzimicrolending.com',
    'https://portal.deghauzimicrolending.com',
    'http://localhost:3000'
)
CORS_ORIGIN_REGEX_WHITELIST = [
    r"^https://\w+\.com$",
    r"^http://\w+\.com$",
    r"^http://\w+\:3000$",
]
CORS_ORIGIN_ALLOW_ALL = False
STATIC_URL = '/staticfiles/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default='')
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
#enforce https
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "De-Ghauzi",

    # Title on the brand, and login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "De-Ghauzi",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/img/logopngs.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Welcome back please login",

    # Copyright on the footer
    "copyright": "De-Ghauzi",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "userprofile.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",
            "permissions": ["userprofile.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "userprofile."},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "userprofile"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"model": "userprofile.User"}
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
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["userprofile", "account", "contributions", "withdrawal"],

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
        "userprofile.User": "fas fa-user",
        "auth.Group": "fas fa-users",
        "withdrawal.Withdrawalrequest": "fab fa-cc-mastercard",
        "userprofile.UserProfile": "fas fa-address-card",
        "account.BankAccountType": "fas fa-code-branch",
        "account.BankAccount": "fas fa-handshake",
        "account.WalletAccount": "fab fa-cc-visa",
        "contributions.DailyContribution": "fas fa-hand-holding-usd",
        "contributions.TargetContribution": "fas fa-money-bill-alt",
        "django.sites": "fab fa-chrome"
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
    "changeform_format": "vertical_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"userprofile.User": "horizontal_tab", "userprofile.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    "language_chooser": False,
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
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-success",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}
