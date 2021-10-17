from datetime import date

from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

from .models import Prestamo
from .forms import PrestamoForm, MultiPrestamoForm

class ListPrestamos(ListView):
    context_object_name = 'lista_prestamos'
    template_name = 'lector/prestamos.html'

    def get_queryset(self):
        return Prestamo.objects.all()
class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        Prestamo.objects.create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False,
        )

        # Actualizo el stock
        libro = form.cleaned_data['libro']
        libro.stock = libro.stock -1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)

class AddPrestamo(FormView):
    # Mismo objetivo que el metodo RegistrarPrestamo 
    # pero con get_or_create para evitar prestar el mismo libro
    # a la misma persona si aun no lo devolvio

    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                'fecha_prestamo': date.today(),
            }
        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')

class AddMultiPrestamo(FormView):

    template_name = 'lector/add_multi_prestamo.html'
    form_class = MultiPrestamoForm
    success_url = '.'

    def form_valid(self, form):

        prestamos = []

        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = l,
                fecha_prestamo = date.today(),
                devuelto = False,
            )
            prestamos.append(prestamo)

        # Guardo en la BD todos los prestamos en BULK
        Prestamo.objects.bulk_create(
            prestamos
        )

        return super(AddMultiPrestamo, self).form_valid(form)
      