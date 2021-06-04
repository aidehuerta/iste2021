from django.db import models

from common.models import BaseModel

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
    teacher = models.ForeignKey(
        'teacher.Teacher', verbose_name='Maestro', on_delete=models.DO_NOTHING, null=True)
    therapist = models.ForeignKey(
        'therapist.Therapist', verbose_name='Terapista', on_delete=models.DO_NOTHING, null=True)
    emotion = models.ForeignKey(
        'session.Emotion', verbose_name='Emoción', on_delete=models.DO_NOTHING)
    notes = models.TextField('Notas', blank=True, null=True)
    observations = models.TextField('Observaciones', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.student} - {self.content}'

    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'
