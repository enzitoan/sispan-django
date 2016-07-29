from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from django.core import serializers

from .forms import DetalleForm
from .models import Detalle

import logging

# Get an instance of a logger
log = logging.getLogger(__name__)

def index(request):    
    return render(request, 'pedido/index.html')    

def pedido(request): 
    if request.method == 'POST':
        log.info("request formulario")
        form = DetalleForm(request.POST)
        log.info("valida formulario")
        if form.is_valid():
            log.info("guardar formulario")
            form.save()
        return redirect('pedido:index')
    else:
        form = DetalleForm()
    return render(request, 'pedido/formulario.html', {'form':form})

def pedido_listado(request):
    pedidos = Detalle.objects.all().order_by('id') 
    context = {'pedidos': pedidos}
    return render(request, 'pedido/listado.html', context)

def pedido_editar(request, id):
    pedido = Detalle.objects.get(id=id)
    if request.method == 'GET':
        form = DetalleForm(instance=pedido)
    else:
        form = DetalleForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
        return redirect('pedido:index')
    context = {
        'form':form,
        'edit': 'S',
    }
    return render(request, 'pedido/formulario.html', )

def pedido_eliminar(request, id):
    pedido = Detalle.objects.get(id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido:pedido_listado')
    return render(request, 'pedido/eliminar.html', {'pedido':pedido})





