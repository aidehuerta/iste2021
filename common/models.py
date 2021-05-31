from django.db import models
from django.utils.translation import ugettext_lazy as _

gender_choices = [
    ('M', _('Hombre')),
    ('F', _('Mujer')),
]


class BaseModel(models.Model):
    created = models.DateTimeField(_('Creado'), auto_now_add=True)
    modified = models.DateTimeField(_('Modificado'), auto_now=True)

    class Meta:
        abstract = True
