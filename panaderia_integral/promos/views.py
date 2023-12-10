from django.shortcuts import render
from .models import Promo

def promos(request):
    promociones = []
    promos = Promo.objects.all()
    for promo in promos:
        promociones.append(promo)
    return render(request, "promos/promos.html", {'promociones': promociones})