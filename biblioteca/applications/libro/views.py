from django.views.generic import ListView, DetailView, TemplateView

from .models import Libro

class HomeView(TemplateView):
    template_name = "home.html"

class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        fecha1 = self.request.GET.get('fecha1', '')
        fecha2 = self.request.GET.get('fecha2', '')

        if fecha1 and fecha2:
            return Libro.objects.listar_by_fechas(palabra_clave, fecha1, fecha2)
        else:
            return Libro.objects.listar(palabra_clave)

class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')

        return Libro.objects.listar_trg(palabra_clave)

class ListLibrosByCategoria(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista_categoria.html'

    def get_queryset(self):
        categoria = self.request.GET.get('categoria', '')
        return Libro.objects.listar_by_categoria(categoria)

class LibroDetailView(DetailView):
    model = Libro
    template_name = 'libro/detalle.html'