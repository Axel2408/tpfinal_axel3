"""tpfinal_axel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from tpfinal_axel.views import primervista, segundavista,diahora_tercervista,nombre_cuartavista, edad_usuario_quintavista, pag_inicio


urlpatterns = [
path('admin/', admin.site.urls),
path('primero/', primervista),
path('segundo/', segundavista),
path('tercero/', diahora_tercervista),
path('cuarto/<nombre>',nombre_cuartavista ), 
path('quinto/<edad>',edad_usuario_quintavista ),
path('inicio/', pag_inicio),
]
    
