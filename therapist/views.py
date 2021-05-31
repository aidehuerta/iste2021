from django.shortcuts import render
from rest_framework import viewsets

from .models import Therapist
from .serializers import TherapistSerializer


class TherapistViewSet(viewsets.ModelViewSet):
    serializer_class = TherapistSerializer
    queryset = Therapist.objects.order_by('name')
