from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .forms import AdicionarTarefaForm
from .models import *
# Create your views here.

def tarefa_home(request):
    contexto = {
        "tarefas":TarefaModel.objects.all()
    }

    return render(request,'escola/TelaInicial.html', contexto)

def tarefa_adicionar(request:HttpRequest):
    if request.method == "POST":
        formulario = AdicionarTarefaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("Escola:home")
    
    contexto = {
        "form": AdicionarTarefaForm
    }
    return render(request,'escola/TelaAdicionar.html', contexto)

def tarefa_remover(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    tarefa.delete()
    return redirect("Escola:home")


def tarefa_editar(request:HttpRequest, id):
    tarefa = get_object_or_404(TarefaModel, id=id)
    if request.method == "POST":
        formulario = AdicionarTarefaForm(request.POST, instance=tarefa)
        if formulario.is_valid():
            formulario.save()
            return redirect("Escola:home")
    formulario = AdicionarTarefaForm(instance = tarefa)
    contexto = {
        'form':formulario
    }
    return render(request, 'escola/TelaEditar.html', contexto)
