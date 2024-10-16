from django.urls import path
from . import views

urlpatterns = [
    path('liste_clients/', views.liste_clients, name='liste_clients'),
]