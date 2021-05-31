from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Usuario"),
        widget=forms.EmailInput({
            'placeholder': _('usuario')}))

    password = forms.CharField(
        label=_("Contraseña"),
        widget=forms.PasswordInput({
            'placeholder': _('contraseña')}))
