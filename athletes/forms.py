from django import forms
from .models import *


class AthletesForm(forms.ModelForm):
    class Meta:
        line_up = forms.ModelChoiceField(queryset=Line_up.objects.filter(id=1))
        model = Athletes
        # fields = ['email', 'first_name', 'last_name', 'middle_name', 'gender', 'tournament', 'phone', 'weight', 'age', 'country', 'region', 'town', 'line_up', 'trainer', 'message']
        fields = '__all__'
        # exclude = ["created", "updated", 'is_active', 'status',]