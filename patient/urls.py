from django.urls import include, path
from rest_framework import routers

from .views import PatientViewSet

app_name = 'patient'

router = routers.DefaultRouter()
router.register(r'', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
]
