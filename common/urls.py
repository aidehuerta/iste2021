from django.urls import path

from .views import description, home, index

app_name = 'common'

urlpatterns = [
    path('', index, name="index"),
    path('description/', description, name="description"),

    path('home/', home, name="home"),
]
