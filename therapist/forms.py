from django import forms

from session.models import Emotion

from .models import Therapist


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
