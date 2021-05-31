from django.contrib import admin

from .models import Emotion, Session

admin.site.register(Emotion)
admin.site.register(Session)
