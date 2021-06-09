from django.urls import path

from .views import add, apply, delete, edit, home

app_name = 'session'

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('apply/<int:pk>/', apply, name='apply'),
    path('delete/<int:pk>/', delete, name='delete'),
]
