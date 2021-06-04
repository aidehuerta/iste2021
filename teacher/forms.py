from django import forms

from session.models import Emotion

from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
        }
