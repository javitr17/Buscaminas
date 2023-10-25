from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("Tablero", views.form_tablero, name="Tablero"),
]