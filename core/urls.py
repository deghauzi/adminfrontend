from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('api/account/',include("account.urls")),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(path('admin/', admin.site.urls))
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)