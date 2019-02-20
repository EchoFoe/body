from django.shortcuts import render
from .forms import *
# from products.models import *


def zayavka_regional(request):


    form = Zayavka_regionalForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()

    return render(request, 'zayavka_regional/zayavka_regional.html', locals())

