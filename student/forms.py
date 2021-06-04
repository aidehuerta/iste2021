from django import forms
from django.forms.widgets import NumberInput

from grade.models import Grade

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'dob': NumberInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-text-input'}),
            'diagnosis': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            'grade': forms.Select(attrs={'class': 'form-text-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        grade = Grade.objects.all()
        grade_display_name = [(_.id, _.name) for _ in grade]
        self.fields['grade'].choices = grade_display_name
