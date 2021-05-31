from django.urls import include, path
from rest_framework import routers

from .views import SessionViewSet

app_name = 'session'

router = routers.DefaultRouter()
router.register(r'', SessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
