from django import forms
from .models import *


class MembersForm(forms.ModelForm):
    class Meta:
        model = Members
        exclude = ["created", "updated"]