from django.db import models

class Autor(models.Model):

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
