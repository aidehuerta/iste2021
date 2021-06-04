from django.db import models

from common.models import BaseModel


class Content(BaseModel):
    """ Videos de contenido """

    title = models.CharField('Título', max_length=100, unique=True)
    url = models.CharField('URL del video', max_length=100)
    description = models.CharField(
        'Descripción', max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'
