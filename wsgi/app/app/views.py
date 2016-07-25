from django.shortcuts import render

def index(request):
    return render(request, 'pedido/pedido.html', {})