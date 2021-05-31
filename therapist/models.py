from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


class Therapist(BaseModel):
    """ Terapistas """

    name = models.CharField(_('Nombre'), max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Terapista')
