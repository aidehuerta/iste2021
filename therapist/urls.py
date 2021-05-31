from django.urls import include, path
from rest_framework import routers

from .views import TherapistViewSet

app_name = 'therapist'

router = routers.DefaultRouter()
router.register(r'', TherapistViewSet, basename='therapist')

urlpatterns = [
    path('', include(router.urls)),
]
