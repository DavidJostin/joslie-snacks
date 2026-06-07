from django.shortcuts import render
from .models import Producto

def catalogo(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, 'catalogo/catalogo.html', {'productos': productos})
