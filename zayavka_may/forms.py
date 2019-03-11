from django import forms
from .models import *


class Zayavka_mayForm(forms.ModelForm):
    class Meta:
        model = Zayavka_may
        exclude = ["created", "updated"]