from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name="libros"),
    path('libros_categoria/', views.ListLibrosByCategoria.as_view(), name="libros_categoria"),
    path('libros/<pk>/', views.LibroDetailView.as_view(), name="libro_detalle"),
]
