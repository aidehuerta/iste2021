from django import forms

from teacher.models import Teacher

from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 60}),
            'teacher': forms.Select(attrs={'class': 'form-text-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['grade'] = forms.IntegerField(min_value=1, max_value=6)

        teacher = Teacher.objects.all()
        teacher_display_name = [(_.id, _.name) for _ in teacher]
        self.fields['teacher'].choices = teacher_display_name
