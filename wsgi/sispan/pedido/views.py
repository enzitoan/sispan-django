from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from django.core import serializers

from .forms import DetalleForm
from .models import Detalle


# HttpResponse para codigo html
# render para renderizar una plantilla

def index(request):
    return render(request, 'pedido/index.html')

def pedido(request):    
    if request.method == 'POST':
        form = DetalleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pedido:pedido_listado')
    else:
        form = DetalleForm()
    return render(request, 'pedido/formulario.html', {'form':form})

def pedido_listado(request):
    pedidos = Detalle.objects.exclude(id=0)    
    return render(request, 'pedido/listado.html', {
        'pedidos': pedidos,
    })

def pedido_editar(request, id):
    pedido = Detalle.objects.get(id=id)
    if request.method == 'GET':
        form = DetalleForm(instance=pedido)
    else:
        form = DetalleForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
        return redirect('pedido:pedido_listado')
    return render(request, 'pedido/formulario.html', {'form':form})

def pedido_eliminar(request, id):
    pedido = Detalle.objects.get(id=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido:pedido_listado')
    return render(request, 'pedido/eliminar.html', {'pedido':pedido})





