from django.db import models

from common.models import BaseModel


class Diagnosis(BaseModel):
    """ Diagnósticos """

    name = models.CharField('Nombre', max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'
