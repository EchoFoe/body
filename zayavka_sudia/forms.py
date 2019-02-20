from django import forms
from .models import *


class Zayavka_sudiaForm(forms.ModelForm):
    class Meta:
        model = Zayavka_sudia
        exclude = ["created", "updated"]