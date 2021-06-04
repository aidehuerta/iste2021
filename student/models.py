from django.db import models

from common.models import BaseModel, gender_choices


class Student(BaseModel):
    """ Estudiantes """

    name = models.CharField('Nombre', max_length=100)
    dob = models.DateField('Fecha de nacimiento')
    gender = models.CharField('Sexo', max_length=1,
                              choices=gender_choices, default='F')
    diagnosis = models.TextField('Diágnostico', blank=True, null=True)
    grade = models.ForeignKey(
        'grade.Grade', verbose_name='Grado', on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudianes'
