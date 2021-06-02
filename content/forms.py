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
            'emotion': forms.Select(attrs={'class': 'form-text-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        emotions = Emotion.objects.all()
        emotions_display_name = [(_.id, _.name) for _ in emotions]
        self.fields['emotion'].choices = emotions_display_name
