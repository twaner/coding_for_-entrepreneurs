__author__ = 'taiowawaner'

from django import forms
from .models import Join


# Forms

class EmailForm(forms.Form):
    email = forms.EmailField()


# Model form

class JoinForm(forms.ModelForm):
    class Meta:
        model = Join
        fields = ["email",]