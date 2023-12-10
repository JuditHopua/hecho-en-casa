from django.shortcuts import render
from promos.models import Promo
from panaderia.models import Product

def pedidos(request):
    productos = Product. objects.all()
    budines = []
    facturas = []
    galletitas = []
    panes = []
    pizzas = []
    tartas = []
    for producto in productos:
        match producto.category_id.name:
            case "Budines":
                budines.append(producto)
            case "Facturas":
                facturas.append(producto)
            case "Galletitas":
                galletitas.append(producto)
            case "Panes":
                panes.append(producto)
            case "Pizzas":
                pizzas.append(producto)
            case _:
                tartas.append(producto)
    promos = Promo.objects.all()
    return render(request, "pedidos/pedidos.html", {'budines': budines, 'facturas': facturas, 'galletitas': galletitas, 'panes': panes, 'pizzas': pizzas, 'tartas': tartas, 'promos': promos})