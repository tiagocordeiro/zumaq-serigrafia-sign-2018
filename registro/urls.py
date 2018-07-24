from django.urls import path

from . import views

urlpatterns = [
    path('', views.visitante_new, name='visitante_new'),
    path('obrigado/', views.visitante_cadastrado, name='visitante_cadastrado'),
    path('sorteio/', views.visitante_sorteio, name='visitante_sorteio'),
]
