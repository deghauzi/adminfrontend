# import os

# from django.core.wsgi import get_wsgi_application
# from whitenoise import WhiteNoise

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.prod")

# application = get_wsgi_application()
# application = WhiteNoise(application)

# import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

application = get_wsgi_application()