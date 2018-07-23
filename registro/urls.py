from django.urls import path

from . import views


urlpatterns = [
    path('', views.visitante_new, name='visitante_new'),
]