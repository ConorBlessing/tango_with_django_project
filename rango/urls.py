from django.urls import path
from rango import views

APP_NAME = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
]