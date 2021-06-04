from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Usuario"),
        widget=forms.TextInput({
            'placeholder': _('Usuario')}))

    password = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput({
            'placeholder': _('Contraseña')}))
