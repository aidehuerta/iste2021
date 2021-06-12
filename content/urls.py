from django.urls import path

from .views import add, delete, edit, home, report

app_name = 'content'

urlpatterns = [
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete'),

    path('report/<int:pk>/', report, name='report'),
]
