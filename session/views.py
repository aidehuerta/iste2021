from django.shortcuts import render
from rest_framework import viewsets

from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.order_by('-id')
