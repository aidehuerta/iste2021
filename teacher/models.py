from django.db import models

from common.models import BaseModel


class Teacher(BaseModel):
    """ Maestros """

    name = models.CharField('Nombre', max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Maestro'
        verbose_name_plural = 'Maestros'
