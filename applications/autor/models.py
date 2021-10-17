from django.db import models

from .managers import AutorManager

class Persona(models.Model):

    NACIONALIDAD_CHOICES = (
        ('1', 'Argentina'),
        ('2', 'Extranjero'),
    )

    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50, choices=NACIONALIDAD_CHOICES)
    fecha_nacimiento = models.DateField('Nacimiento')

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre + ' ' + self.apellido


class Autor(Persona):
    seudonimo = models.CharField(
        max_length=50, 
        blank=True, 
    )

    objects = AutorManager()
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


