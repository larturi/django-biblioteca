from django.db import models

from applications.libro.models import Libro

class Lector(models.Model):

    NACIONALIDAD_CHOICES = (
        ('1', 'Argentina'),
        ('2', 'Extranjero'),
    )

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    macionalidad = models.CharField('Nacionalidad', max_length=50, choices=NACIONALIDAD_CHOICES)
    fecha_nacimiento = models.DateField('Nacimiento')

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def __str__(self):
        return self.libro.titulo