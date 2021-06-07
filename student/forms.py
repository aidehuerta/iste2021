from django import forms
from django.forms.widgets import NumberInput

from group.models import Group
from diagnosis.models import Diagnosis

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'dob': NumberInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-text-input'}),
            'diagnosis': forms.Select(attrs={'class': 'form-text-input'}),
            'group': forms.Select(attrs={'class': 'form-text-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        group = Group.objects.all()
        group_display_name = [(_.id, _.name) for _ in group]
        self.fields['group'].choices = group_display_name

        diagnosis = Diagnosis.objects.all()
        diagnosis_display_name = [(_.id, _.name) for _ in diagnosis]
        self.fields['diagnosis'].choices = diagnosis_display_name
