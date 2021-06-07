from django.db import models

from common.models import BaseModel, gender_choices


class Student(BaseModel):
    """ Estudiantes """

    name = models.CharField('Nombre', max_length=100)
    dob = models.DateField('Fecha de nacimiento')
    gender = models.CharField(
        'Sexo', max_length=1, choices=gender_choices, default='F')
    diagnosis = models.ForeignKey(
        'diagnosis.Diagnosis', verbose_name='Diagnóstico', on_delete=models.DO_NOTHING, null=True)
    group = models.ForeignKey(
        'group.Group', verbose_name='Grupo', on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudianes'
