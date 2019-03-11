from django import forms
from .models import *


class Zayavka_juneForm(forms.ModelForm):
    class Meta:
        model = Zayavka_june
        exclude = ["created", "updated"]