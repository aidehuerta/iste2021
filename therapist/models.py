from django.db import models

from common.models import BaseModel


class Therapist(BaseModel):
    """ Terapistas """

    name = models.CharField('Nombre', max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Terapeuta'
        verbose_name_plural = 'Terapeutas'
