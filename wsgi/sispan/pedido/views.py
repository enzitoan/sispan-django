from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Pan, Detalle

# HttpResponse para codigo html
# render para renderizar una plantilla

#def index(request):
#   return HttpResponse('<p>In index view</p>')

def index(request):
    panes = Pan.objects.exclude(id=0)    
    return render(request, 'pedido/index.html', {
        'panes': panes,
    })

#def detalle(request, id):
#   return HttpResponse('<p>In pan_detail view with id {0}</p>'.format(id))

def detalle(request, id):
    try:
        pan = Pan.objects.get(id=id)
    except pan.DoesNotExist:
        raise Http404('El pan no existe')
    return render(request, 'pedido/detalle.html', {
        'pan': pan,
    })

def agregar(request):
    return render(request, 'pedido/agregar.html', {})

def guardar(request):
    pan = Pan()
    pan.nombre = request.POST['tipo']
    pan.valor = request.POST['valor']
    pan.descripcion = request.POST['descripcion']
    
    pan.save()

    panes = Pan.objects.exclude(id=0)    
    return render(request, 'pedido/index.html', {
        'panes': panes,
    })

def guardar_detalle(request):    
    detalle = Detalle()
    detalle.nombre = request.POST['nombre']
    detalle.email = request.POST['email']
    detalle.cantidad_pita_integral = request.POST['pan_pi']
    detalle.cantidad_pita_blanco = request.POST['pan_pb']
    detalle.cantidad_amasado_integral = request.POST['pan_ai']
    detalle.cantidad_amasado_blanco = request.POST['pan_ab']
    detalle.save()

    response = """
        <script type='text/javascript'>
            alert('Pedido Recepcionado');
            document.location.href = '/sispan/pedido.html';
        </script>
    """

    return HttpResponse(response)
    
def eliminar(request, id):
    try:
        pan = Pan.objects.get(id=id)
    except pan.DoesNotExist:
        raise Http404('El pan no existe')

    pan = Pan.objects.get(id=id)
    pan.delete()

    panes = Pan.objects.exclude(id=0)    
    return render(request, 'pedido/index.html', {
        'panes': panes,
    })

def pedido(request):
    return render(request, 'pedido/pedido.html', {})

