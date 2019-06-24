from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r'^', include('landing.urls')),
    url(r'^', include('zayavka.urls')),
    url(r'^', include('zayavka_regional.urls')),
    url(r'^', include('zayavka_sudia.urls')),
    url(r'^', include('zayavka_may.urls')),
    url(r'^', include('zayavka_june.urls')),
    url(r'^', include('news.urls')),
    url(r'^', include('tournaments.urls')),
    url(r'^', include('athletes.urls')),
    url(r'^', include('sportsman.urls')),
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

