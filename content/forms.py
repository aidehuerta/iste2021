from django import forms

from session.models import Emotion

from .models import Content


class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        emotions = Emotion.objects.all()
        emotions_display_name = [(g.id, g.name) for g in emotions]
        self.fields['emotion'].choices = emotions_display_name
