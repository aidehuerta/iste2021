from django.db import models

from common.models import BaseModel


class Grade(BaseModel):
    """ Materias """

    name = models.CharField('Nombre', max_length=100)
    grade = models.SmallIntegerField('Grado', null=True)
    teacher = models.ForeignKey(
        'teacher.Teacher', verbose_name='Maestro', on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.grade}'

    class Meta:
        verbose_name = 'Grado'
        verbose_name_plural = 'Grados'
