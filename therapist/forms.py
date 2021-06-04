from django import forms

from .models import Therapist


class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
        }
