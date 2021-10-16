from django.db import models
from django.db.models.signals import post_delete

from .managers import *
from applications.libro.models import Libro
from applications.autor.models import Persona

class Lector(Persona):
       class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"

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

    def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock -1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def __str__(self):
        return self.libro.titulo

def update_libro_stock(sender, instance, **kwargs):
    # Actualiza el stock si se elimina un prestamo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()

post_delete.connect(update_libro_stock, sender=Prestamo)