"""
URL configuration for panaderia_integral project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from panaderia import views as panaderia_views
from promos import views as promos_views
from pedidos import views as pedidos_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('budines', panaderia_views.budines, name='budines'),
    path('facturas', panaderia_views.facturas, name='facturas'),
    path('galletitas', panaderia_views.galletitas, name='galletitas'),
    path('panes', panaderia_views.panes, name='panes'),
    path('pizzas', panaderia_views.pizzas, name='pizzas'),
    path('tartas', panaderia_views.tartas, name='tartas'),
    path('promos', promos_views.promos, name='promos'),
    path('pedidos', pedidos_views.pedidos, name='pedidos'),
    path('consejos', core_views.consejos, name='consejos'),
    path('contacto', core_views.contacto, name='contacto'),
    path('donde-nos-encontras', core_views.donde_nos_encontras, name='donde_nos_encontras'),
    path('quienes-somos', core_views.quienes_somos, name='quienes_somos'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
