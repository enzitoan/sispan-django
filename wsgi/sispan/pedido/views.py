from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pan, Detalle

# HttpResponse para codigo html
# render para renderizar una plantilla

#def index(request):
#   return HttpResponse('<p>In index view</p>')

def index(request):
    pedidos = Detalle.objects.exclude(id=0)    
    return render(request, 'pedido/listado.html', {
        'pedidos': pedidos,
    })

#def detalle(request, id):
#   return HttpResponse('<p>In pan_detail view with id {0}</p>'.format(id))

def detalle(request, id):
    try:
        pedido = Detalle.objects.get(id=id)
    except pedido.DoesNotExist:
        raise Http404('El pan no existe')
    return render(request, 'pedido/detalle.html', {
        'pedido': pedido,
    })

# def agregar(request):
#     return render(request, 'pedido/agregar.html', {})

# def guardar(request):
#     pan = Pan()
#     pan.nombre = request.POST['tipo']
#     pan.valor = request.POST['valor']
#     pan.descripcion = request.POST['descripcion']
    
#     pan.save()

#     panes = Pan.objects.exclude(id=0)    
#     return render(request, 'pedido/index.html', {
#         'panes': panes,
#     })

def guardar_detalle(request):    
    pedido = Detalle()
    pedido.nombre = request.POST['nombre']
    pedido.email = request.POST['email']
    pedido.cantidad_pita_integral = request.POST['pan_pi']
    pedido.cantidad_pita_blanco = request.POST['pan_pb']
    pedido.cantidad_amasado_integral = request.POST['pan_ai']
    pedido.cantidad_amasado_blanco = request.POST['pan_ab']
    pedido.save()

    response = """
        <script type='text/javascript'>
            alert('Pedido Recepcionado');
            document.location.href = '/sispan/pedido/';
        </script>
    """

    return HttpResponse(response)
    
def eliminar(request, id):
    try:
        pedido = Detalle.objects.get(id=id)
    except pedido.DoesNotExist:
        raise Http404('El pedido no existe')

    pedido = Detalle.objects.get(id=id)
    pedido.delete()

    pedidos = Detalle.objects.exclude(id=0)    
    return render(request, 'pedido/index.html', {
        'pedidos': pedidos,
    })

def pedido(request):
    return render(request, 'pedido/pedido.html', {})

