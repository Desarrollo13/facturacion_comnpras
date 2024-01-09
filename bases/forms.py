from collections.abc import Mapping
from typing import Any
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Usuario
from django.forms import fields
from django import forms
from django.forms.widgets import PasswordInput


class UsuarioCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = ("email",)


class UsuarioChangeForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(UsuarioChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Usuario
        fields = '__all__'


class Userform(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)

    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'password']
        widget = {'email': forms.EmailInput, 'password': forms.PasswordInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
