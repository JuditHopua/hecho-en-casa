from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def consejos(request):
    return render(request, "core/consejos.html")

def contacto(request):
    return render(request, "core/contacto.html")

def donde_nos_encontras(request):
    return render(request, "core/donde_nos_encontras.html")

def quienes_somos(request):
    return render(request, "core/quienes_somos.html")