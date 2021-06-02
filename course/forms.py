from django import forms

from teacher.models import Teacher
from therapist.models import Therapist

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 30}),
            'teacher': forms.Select(attrs={'class': 'form-text-input'}),
            'therapist': forms.Select(attrs={'class': 'form-text-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['level'] = forms.IntegerField(min_value=1, max_value=6)

        teacher = Teacher.objects.all()
        teacher_display_name = [(_.id, _.name) for _ in teacher]
        self.fields['teacher'].choices = teacher_display_name

        therapist = Therapist.objects.all()
        therapist_display_name = [(_.id, _.name) for _ in therapist]
        self.fields['therapist'].choices = therapist_display_name
