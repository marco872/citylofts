# citylofts_app/urls.py

from django.urls import path
from . import views

app_name = 'citylofts_apps'

urlpatterns = [
    path('', views.index, name='index'),

    path('lofts-rental/', views.lofts_rental_view, name='lofts_rental'), 
    path('temporary-stands-rental/', views.temporary_stand_rental_view, name='temporary_stand_rental'),
    path('co-minimizing/', views.co_minimizing_view, name='co_minimizing'),
]
