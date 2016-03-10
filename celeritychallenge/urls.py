""" Weatherapp URL Configuration """
# Standard lib imports
# Third party imports
# Local imports
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.demo.urls', namespace='demo', app_name='demo')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
