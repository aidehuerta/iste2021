from django import forms

from session.models import Emotion

from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'size': 30}),
            'url': forms.TextInput(attrs={'size': 60}),
            'description': forms.TextInput(attrs={'size': 60}),
        }
