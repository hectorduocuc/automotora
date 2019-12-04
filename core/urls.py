from django.urls import path
from .views import home, galeria, formulario, listar_automoviles, eliminar_automovil, modificar_automovil, contacto





urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('listar-autos/', listar_automoviles, name="listado_automoviles"),
    path('eliminar-auto/<id>/', eliminar_automovil, name="eliminar_automovil"),
    path('modificar-auto/<id>/', modificar_automovil, name="modificar_automovil"),
    path('contacto/', contacto, name="contacto"),

    
]