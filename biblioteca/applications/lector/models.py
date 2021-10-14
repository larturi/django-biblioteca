from django.db import models
from .managers import *
from applications.libro.models import Libro

class Lector(models.Model):

    NACIONALIDAD_CHOICES = (
        ('1', 'Argentina'),
        ('2', 'Extranjero'),
    )

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50, choices=NACIONALIDAD_CHOICES)
    fecha_nacimiento = models.DateField('Nacimiento')
    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"

    def __str__(self):
        return self.nombre + ' ' + self.apellido
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def __str__(self):
        return self.libro.titulo