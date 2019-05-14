from django.conf.urls import url, include
from django.contrib import admin
from tournaments import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [

    url(r'^tournament_(?P<tournament_id>\w+)/$', views.tournament, name='tournament'),

]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
