from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel, gender_choices


class Patient(BaseModel):
    """ Pacientes """

    name = models.CharField(_('Nombre'), max_length=100)
    dob = models.DateField(_('Fecha de nacimiento'))
    gender = models.CharField(_('Sexo'), max_length=1,
                              choices=gender_choices, default='F')
    diagnosis = models.TextField(_('Diágnostico'), blank=True, null=True)
    course = models.ForeignKey('course.Course', verbose_name=_(
        'Materia'), on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Paciente')
