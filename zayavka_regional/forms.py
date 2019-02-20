from django import forms
from .models import *


class Zayavka_regionalForm(forms.ModelForm):
    class Meta:
        model = Zayavka_regional
        exclude = ["created", "updated"]