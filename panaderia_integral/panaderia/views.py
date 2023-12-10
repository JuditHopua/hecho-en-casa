from django.shortcuts import render
from .models import Product

def budines(request):
    productos = Product.objects.filter(category_id__name="Budines")
    if productos.exists:
        categoria = "Budines"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})

def facturas(request):
    productos = Product.objects.filter(category_id__name="Facturas")
    if productos.exists:
        categoria = "Facturas"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})

def galletitas(request):
    productos = Product.objects.filter(category_id__name="Galletitas")
    if productos.exists:
        categoria = "Galletitas"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})

def panes(request):
    productos = Product.objects.filter(category_id__name="Panes")
    if productos.exists:
        categoria = "Panes"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})

def pizzas(request):
    productos = Product.objects.filter(category_id__name="Pizzas")
    if productos.exists:
        categoria = "Pizzas"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})

def tartas(request):
    productos = Product.objects.filter(category_id__name="Tartas")
    if productos.exists:
        categoria = "Tartas"
    else:
        categoria = productos.first().category_id.name
    return render(request, "panaderia/productos.html", {'productos': productos, 'categoria': categoria})