from django.urls import path

from .views import add, delete, edit, home

app_name = 'teacher'

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
]
