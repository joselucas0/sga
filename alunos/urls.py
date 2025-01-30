from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/aluno/', views.cadastro_aluno, name='cadastro_aluno'),
    path('cadastro/avaliacao/', views.cadastro_avaliacao, name='cadastro_avaliacao'),
    path('relatorio/', views.relatorio, name='relatorio'),
]