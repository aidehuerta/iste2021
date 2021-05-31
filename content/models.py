from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


class Content(BaseModel):
    """ Videos de contenido """

    title = models.CharField(_('Título'), max_length=100, unique=True)
    url = models.CharField(_('URL del video'), max_length=100)
    description = models.CharField(
        _('Descripción'), max_length=100, blank=True, null=True)
    emotion = models.ForeignKey('session.Emotion', verbose_name=_(
        'Emoción'), on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Contenido')
