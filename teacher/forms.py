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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
