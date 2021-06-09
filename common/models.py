from django.db import models
from django.contrib.auth.models import User


gender_choices = [
    ('M', 'Hombre'),
    ('F', 'Mujer'),
]


department_choices = [
    ('DP', 'Disciplina Positiva'),
    ('DO', 'Docente'),
    ('PS', 'Psicopedagógico'),
]


class BaseModel(models.Model):
    created = models.DateTimeField('Creado', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(
        'Departamento', max_length=2, choices=department_choices)
