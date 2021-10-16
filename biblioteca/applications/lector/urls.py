from django.urls import path

from . import views

urlpatterns = [
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
