from django.db import models

gender_choices = [
    ('M', 'Hombre'),
    ('F', 'Mujer'),
]


class BaseModel(models.Model):
    created = models.DateTimeField('Creado', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        abstract = True
