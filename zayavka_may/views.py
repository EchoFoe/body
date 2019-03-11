from django.shortcuts import render
from .forms import *
# from products.models import *


def zayavka_may(request):

    form = Zayavka_mayForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()

    return render(request, 'zayavka_may/zayavka_may.html', locals())

