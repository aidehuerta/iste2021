from django import forms

from .models import Diagnosis


class DiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 60}),
        }
