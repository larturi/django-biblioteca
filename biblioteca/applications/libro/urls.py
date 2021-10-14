from django.urls import path

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name="libros"),
    path('libros-trg/', views.ListLibrosTrg.as_view(), name="libros-trg"),
    path('libros-categoria/', views.ListLibrosByCategoria.as_view(), name="libros-categoria"),
    path('libros/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"),
]
