
from django import forms

from .models import Film


class MovieForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'year', 'image', 'description']


