from dataclasses import field
from django import forms

from .models import *

class ImgForm(forms.ModelForm):

    class Meta:
        model = magaz
        fields = ['name', 'img']