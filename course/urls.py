from django.urls import include, path
from rest_framework import routers

from .views import CourseViewSet

app_name = 'course'

router = routers.DefaultRouter()
router.register(r'', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
