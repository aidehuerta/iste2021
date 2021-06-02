from django.urls import path

from .views import add, delete, edit, listing

app_name = 'content'

urlpatterns = [
    path('', listing, name='home'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),
]
