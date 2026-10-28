from django.urls import path

from .views.categoria import (
    actualizar_categoria,
    agregar_categoria,
    eliminar_categoria,
    lista_categorias,
)


urlpatterns = [
    path("", lista_categorias, name="inicio"),
    path("categoria/", lista_categorias, name="list_categorias"),
    path("categoria/add/", agregar_categoria, name="add_categoria"),
    path(
        "categoria/<int:id>/update/",
        actualizar_categoria,
        name="update_categoria",
    ),
    path(
        "categoria/<int:id>/delete/",
        eliminar_categoria,
        name="delete_categoria",
    ),
]
