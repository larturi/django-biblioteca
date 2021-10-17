from django.urls import path

from . import views

app_name = "lector_app"

urlpatterns = [
    path(
        'prestamos', 
        views.ListPrestamos.as_view(), 
        name="prestamos"
    ),
    path(
        'prestamo/add/', 
        views.AddPrestamo.as_view(), 
        name="prestamo-add"
    ),
    path(
        'prestamo_multiple/add/', 
        views.AddMultiPrestamo.as_view(), 
        name="multiprestamo-add"
    ),
]
