from django.urls import path

from .views import add_content, delete_content, edit_content, list_content

app_name = 'content'

urlpatterns = [
    path('', list_content, name='list'),
    path('add/', add_content, name='add'),
    path('edit/<int:pk>/', edit_content, name='edit'),
    path('delete/<int:pk>/', delete_content, name='delete'),
]
