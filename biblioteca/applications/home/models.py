from django.db import models

class Persona(models.Model):
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    pais = models.CharField('Pais', max_length=100)
    pasaporte = models.CharField('Pasaporte', max_length=100)
    edad = models.IntegerField('Edad')
    nick = models.CharField('Nick', max_length=10)
    
    class Meta:
        abstract = True
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        unique_together = ['pais', 'nick']
        # constraints = [
        #     models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        # ]

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Empleado(Persona):

    SENIORITY_CHOICES = (
        ('1', 'Junior'),
        ('2', 'Semi-Senior'),
        ('3', 'Senior'),
    )

    puesto = models.CharField('Puesto', max_length=100)
    seniority = models.CharField('Seniority', max_length=20, choices=SENIORITY_CHOICES)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


class Cliente(Persona):
    empresa = models.CharField('Empresa', max_length=100)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
