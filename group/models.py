from django.db import models

from common.models import BaseModel


level_choices = [
    ('K', 'Kinder'),
    ('P', 'Primaria'),
]


class Group(BaseModel):
    """ Grupos """

    name = models.CharField('Nombre', max_length=100)
    level = models.CharField(
        'Nivel', max_length=1, choices=level_choices, default='K')
    grade = models.SmallIntegerField('Grado', null=True)
    teacher = models.ForeignKey(
        'teacher.Teacher', verbose_name='Maestro', on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.grade}'

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
