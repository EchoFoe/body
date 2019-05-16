from django import forms
from django.shortcuts import render
from .forms import *
from .models import *


def athletes_bid(request):

    # tournaments = Athletes.objects.filter(tournament__tournaments_status_id=1)
    # tournaments = Athletes.objects.get(tournament__tournaments_status_id=1)

    form = AthletesForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()

    return render(request, 'athletes_bid/athletes_bid.html', locals())