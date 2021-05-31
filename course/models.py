from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


class Course(BaseModel):
    """ Materias """

    name = models.CharField(_('Nombre'), max_length=100)
    level = models.SmallIntegerField(_('Grado'), null=True)
    teacher = models.ForeignKey('teacher.Teacher', verbose_name=_(
        'Maestro'), on_delete=models.DO_NOTHING, null=True)
    terapist = models.ForeignKey('therapist.Therapist', verbose_name=_(
        'Terapista'), on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.level}'

    class Meta:
        verbose_name = _('Materia')
