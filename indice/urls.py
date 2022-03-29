from .views import inicio,otra_vista,numero_random,mi_plantilla
from django.urls import path

urlpatterns=[  
    path('',inicio, name='inicio'),
    path('otra_vista/',otra_vista, name='otra_vista'),
    path('mi_plantilla/',mi_plantilla,name='mi_plantilla'),]