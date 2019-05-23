from django.shortcuts import render
from .forms import *
from news.models import *
from tournaments.models import *
from representative.models import *
from documents.models import *


def home(request):

    news_images = NewsImage.objects.filter(mews_image_is_active=True, news_image_is_main=True, News__news_is_active=True)
    news_images_1 = news_images.filter(News__news_category__id=1)

    tournaments_view = Tournaments.objects.filter(tournaments_is_active=True)
    tournaments_view_new = tournaments_view.filter(tournaments_status_id=1)
    tournaments_view_held = tournaments_view.filter(tournaments_status__is_active=True, tournaments_status_id=2)
    tournaments_view_canceled = tournaments_view.filter(tournaments_status_id=3)
    tournaments_view_failed = tournaments_view.filter(tournaments_status_id=4)

    representative_images = RepresentativeImage.objects.filter(image_is_active=True, image_is_main=True)
    representative_images_all = representative_images.filter(Representative__is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()

    return render(request, 'landing/home.html', locals())

def news(request):

    news_images = NewsImage.objects.filter(mews_image_is_active=True, news_image_is_main=True,
                                           News__news_is_active=True)
    news_images_1 = news_images.filter(News__news_category__id=1)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'news/news.html', locals())


def calendar(request):

    tournaments_view = Tournaments.objects.filter(tournaments_is_active=True)
    tournaments_view_new = tournaments_view.filter(tournaments_status_id=1)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'calendar/calendar.html', locals())

def documents(request):

    # documents_view = Documents.objects.filter(documents_is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'documents/documents.html', locals())

def on_line(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'on_line/on_line.html', locals())

def representative(request):

    representative_images = RepresentativeImage.objects.filter(image_is_active=True, image_is_main=True)
    representative_images_all = representative_images.filter(Representative__is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'representative/representative.html', locals())

def about_us(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'about_us/about_us.html', locals())

def lk(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'lk/lk.html', locals())

def broadcast(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'broadcast/broadcast.html', locals())

def club(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'club/club.html', locals())