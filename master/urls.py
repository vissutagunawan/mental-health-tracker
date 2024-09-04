from django.urls import path, include
from master.views import show_main

app_name = 'master'

urlpatterns = [
    path('', show_main, name='main'),
]