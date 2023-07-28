# citylofts_app/urls.py

from django.urls import path
from . import views

app_name = 'citylofts_apps'

urlpatterns = [
    path('', views.index, name='index'),
]