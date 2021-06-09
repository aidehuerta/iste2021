from common.models import Employee
from django import forms
from django.contrib.auth import get_user_model

from content.models import Content
from session.models import Emotion
from student.models import Student

from .models import Session

User = get_user_model()


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        widgets = {
            'student': forms.Select(attrs={'class': 'form-text-input'}),
            'content': forms.Select(attrs={'class': 'form-text-input'}),
            'user': forms.Select(attrs={'class': 'form-text-input emotion white'}),
            'notes': forms.Textarea(attrs={'cols': 63, 'rows': 5}),
            'observations': forms.Textarea(attrs={'cols': 63, 'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields['emotion'].required = False
        self.fields['emotion'].disabled = True

        employee = Employee.objects.filter(user=user).first()

        student = Student.objects.all()
        if employee is not None and employee.department == 'DO':
            student = student.filter(group__user=user)
        student_display_name = [(_.id, _.name) for _ in student]
        self.fields['student'].choices = student_display_name

        content = Content.objects.all()
        content_display_name = [(_.id, _.title) for _ in content]
        self.fields['content'].choices = content_display_name

        if self.instance.id is not None:
            user_display_name = [
                (self.instance.user.id, f'{self.instance.user.first_name} {self.instance.user.last_name}')]
        else:
            user_display_name = [
                (user.id, f'{user.first_name} {user.last_name}')]
        self.fields['user'].choices = user_display_name

        form_control = 'form-text-input emotion '
        if self.instance.emotion_id == 1:
            form_control += 'green'
        elif self.instance.emotion_id == 2:
            form_control += 'blue'
        elif self.instance.emotion_id == 3:
            form_control += 'red'
        elif self.instance.emotion_id == 4:
            form_control += 'yellow'
        else:
            form_control += 'white'
        self.fields['emotion'].widget.attrs.update({'class': form_control})


class SessionApplyForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('emotion',)
        widgets = {
            'emotion': forms.Select(attrs={'type': 'hidden'}),
        }
