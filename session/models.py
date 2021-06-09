from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel

User = get_user_model()

color_choices = [
    ('yellow', 'Amarillo'),
    ('blue', 'Azul'),
    ('red', 'Rojo'),
    ('black', 'Negro'),
    ('green', 'Verde'),
]


class Emotion(BaseModel):
    """ Emociones """

    name = models.CharField('Nombre', max_length=100)
    color = models.CharField('Color', max_length=10,
                             choices=color_choices, null=True)
    description = models.TextField('Descripción', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Emoción'
        verbose_name_plural = 'Emociones'


class Session(BaseModel):
    """ Sesiones """

    student = models.ForeignKey(
        'student.Student', verbose_name='Estudiante', on_delete=models.DO_NOTHING)
    content = models.ForeignKey(
        'content.Content', verbose_name='Contenido', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(
        User, verbose_name='Aplica', on_delete=models.DO_NOTHING)
    emotion = models.ForeignKey(
        'session.Emotion', verbose_name='Emoción', on_delete=models.DO_NOTHING, null=True)
    notes = models.TextField('Notas', blank=True, null=True)
    observations = models.TextField('Observaciones', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.student} - {self.content}'

    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'
