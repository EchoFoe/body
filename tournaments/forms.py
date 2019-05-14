from django import forms
from .models import *

class MovieChangeListForm(forms.ModelForm):

    tournaments_divisions = forms.ModelMultipleChoiceField(
        queryset=TournamentsDivision.objects.all(), required=False)