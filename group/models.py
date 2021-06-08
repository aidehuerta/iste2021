from django.db import models
from django.contrib.auth import get_user_model

from common.models import BaseModel

User = get_user_model()

level_choices = [
    ('PK', 'Preschool'),
    ('MD', 'Middle school'),
]


class Group(BaseModel):
    """ Grupos """

    name = models.CharField('Nombre', max_length=100)
    level = models.CharField(
        'Nivel', max_length=2, choices=level_choices, default='PK')
    grade = models.SmallIntegerField('Grado', null=True)
    user = models.ForeignKey(
        User, verbose_name='Maestro', on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.grade}'

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
