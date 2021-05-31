from django.urls import include, path
from rest_framework import routers

from .views import TeacherViewSet

app_name = 'teacher'

router = routers.DefaultRouter()
router.register(r'', TeacherViewSet, basename='teacher')

urlpatterns = [
    path('', include(router.urls)),
]
