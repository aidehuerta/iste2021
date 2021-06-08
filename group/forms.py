from django import forms

from django.contrib.auth import get_user_model
from .models import Group

User = get_user_model()


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'size': 60}),
            'level': forms.Select(attrs={'class': 'form-text-input'}),
            'user': forms.Select(attrs={'class': 'form-text-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['grade'] = forms.IntegerField(min_value=1, max_value=6)

        users = User.objects.filter(employee__department='DO')
        user_display_name = [
            (_.id, f'{_.first_name} {_.last_name}') for _ in users]
        self.fields['user'].choices = user_display_name
