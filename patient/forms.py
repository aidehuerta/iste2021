from django import forms
from django.forms.widgets import NumberInput

from course.models import Course

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'dob': NumberInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-text-input'}),
            'diagnosis': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            'course': forms.Select(attrs={'class': 'form-text-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        course = Course.objects.all()
        course_display_name = [(_.id, _.name) for _ in course]
        self.fields['course'].choices = course_display_name
