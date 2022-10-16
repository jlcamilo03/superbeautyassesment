from inventario.views import ListaEquipo
from django.urls import path

urlpatterns = [
    path('', ListaEquipo.as_view()),
]