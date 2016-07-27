from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404

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
        detalle = DetalleForm(request.POST)

        if form.is_valid():
            detalle.save()
            response = """
                <script type='text/javascript'>
                    alert('Pedido Recepcionado');
                </script>
            """
        else:
            response = """
                <script type='text/javascript'>
                    alert('Error');
                </script>
            """            

        return redirect('sispan:pedido')

    else:
        detalle = DetalleForm()

    return HttpResponse(response)

    # detalle = Detalle()
    # detalle.nombre = request.POST['nombre']        
    # detalle.email = request.POST['email']
    # detalle.cantidad_pita_integral = request.POST['pan_pi']
    # detalle.cantidad_pita_blanco = request.POST['pan_pb']
    # detalle.cantidad_amasado_integral = request.POST['pan_ai']
    # detalle.cantidad_amasado_blanco = request.POST['pan_ab']
    # detalle.save()

    # response = """
    #     <script type='text/javascript'>
    #         alert('Pedido Recepcionado');
    #         document.location.href = '/sispan/pedido/';
    #     </script>
    # """

    # return HttpResponse(response)


