from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

from django.core import serializers

from .forms import DetalleForm
from .models import Detalle


# HttpResponse para codigo html
# render para renderizar una plantilla

def index(request):
    pedidos = Detalle.objects.exclude(id=0)    
    return render(request, 'pedido/index.html', {
        'pedidos': pedidos,
    })

def pedido(request):
    return render(request, 'pedido/pedido.html', {})

def detalle(request, id):
    try:
        detalle = Detalle.objects.get(id=id)
    except Detalle.DoesNotExist:
        raise Http404('El detalle no existe')
    return render(request, 'pedido/detalle.html', {
        'detalle': detalle,
    })
    
def eliminar(request, id):
    try:
        detalle = Detalle.objects.get(id=id)
    except Detalle.DoesNotExist:
        raise Http404('El detalle no existe')

    detalle = Detalle.objects.get(id=id)
    detalle.delete()

    pedidos = Detalle.objects.exclude(id=0)    
    return render(request, 'pedido/listado.html', {
        'pedidos': pedidos,
    })

def guardar_detalle(request): 
    if request.method == 'POST':
        form = DetalleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pedido:index')
    else:
        form = DetalleForm()

    return render(request, 'pedido/pedido_form.html', {'form':form})


