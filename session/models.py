from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel

color_choices = [
    ('yellow', _('Amarillo')),
    ('blue', _('Azul')),
    ('red', _('Rojo')),
    ('black', _('Negro')),
    ('green', _('Verde')),
]


class Emotion(BaseModel):
    """ Emociones """

    name = models.CharField(_('Nombre'), max_length=100)
    color = models.CharField(_('Color'), max_length=10,
                             choices=color_choices, null=True)
    description = models.TextField(_('Descripción'), blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Emoción')
        verbose_name_plural = _('Emociones')


class Session(BaseModel):
    """ Sesiones """

    patient = models.ForeignKey('patient.Patient', verbose_name=_(
        'Paciente'), on_delete=models.DO_NOTHING)
    content = models.ForeignKey('content.Content', verbose_name=_(
        'Contenido'), on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('teacher.Teacher', verbose_name=_(
        'Maestro'), on_delete=models.DO_NOTHING, null=True)
    therapist = models.ForeignKey('therapist.Therapist', verbose_name=_(
        'Terapista'), on_delete=models.DO_NOTHING, null=True)
    emotion = models.ForeignKey('session.Emotion', verbose_name=_(
        'Emoción'), on_delete=models.DO_NOTHING)
    notes = models.TextField(_('Notas'), blank=True, null=True)
    observations = models.TextField(_('Observaciones'), blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.patient} - {self.content}'

    class Meta:
        verbose_name = _('Sesión')
        verbose_name_plural = _('Sesiones')
