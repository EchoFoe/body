""" URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    # url(r'^product-details/$', views.product, name='product-details'),
    # url(r'^checkout/$', views.checkout, name='checkout'),
    # url(r'^shop-cart/$', views.cart, name='shop-cart'),
    # url(r'^magazine/$', views.magazine, name='magazine'),
    # url(r'^pis/$', views.pis, name='proektirovanie'),
    # url(r'^bmk/$', views.bmk, name='bmk'),
    url(r'^representative/$', views.representative, name='representative'),
    url(r'^news/$', views.news, name='news'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^documents/$', views.documents, name='documents'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    # url(r'^kvartiri/$', views.kvartiri, name='kvartiri'),
    url(r'^$', views.home, name='home'),

] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
