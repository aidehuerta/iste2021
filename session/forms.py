from django import forms
from django.forms.widgets import NumberInput

from content.models import Content
from patient.models import Patient
from teacher.models import Teacher
from therapist.models import Therapist
from session.models import Emotion

from .models import Session


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-text-input'}),
            'content': forms.Select(attrs={'class': 'form-text-input'}),
            'teacher': forms.Select(attrs={'class': 'form-text-input'}),
            'therapist': forms.Select(attrs={'class': 'form-text-input'}),
            'emotion': forms.Select(attrs={'class': 'form-text-input'}),
            'notes': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
            'observations': forms.Textarea(attrs={'cols': 60, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        patient = Patient.objects.all()
        patient_display_name = [(_.id, _.patient) for _ in patient]
        self.fields['patient'].choices = patient_display_name

        content = Content.objects.all()
        content_display_name = [(_.id, _.patient) for _ in content]
        self.fields['content'].choices = content_display_name

        teacher = Teacher.objects.all()
        teacher_display_name = [(_.id, _.name) for _ in teacher]
        self.fields['teacher'].choices = teacher_display_name

        therapist = Therapist.objects.all()
        therapist_display_name = [(_.id, _.name) for _ in therapist]
        self.fields['therapist'].choices = therapist_display_name

        emotions = Emotion.objects.all()
        emotions_display_name = [(_.id, _.name) for _ in emotions]
        self.fields['emotion'].choices = emotions_display_name
