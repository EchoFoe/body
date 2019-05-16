from django.shortcuts import render
from .forms import *


def zayavka_june(request):

    form = Zayavka_juneForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()

    return render(request, 'zayavka_june/zayavka_june.html', locals())

