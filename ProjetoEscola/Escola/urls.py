from django.urls import path
from . import views

app_name= "Escola"

urlpatterns = [
    path('', views.tarefa_home, name='home'),
    path('Adicionar/', views.tarefa_adicionar, name='adiciona'),
    path('Remover/<int:id>', views.tarefa_remover, name='remover'),
    path('Editar/<int:id>', views.tarefa_editar, name='editar')
]