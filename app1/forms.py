from django import forms
from .models import Appmodel


class Appform(forms.ModelForm):
    class Meta:
        model=Appmodel
        fields='__all__'