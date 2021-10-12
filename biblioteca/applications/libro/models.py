from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager
class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length=50)

    objects = CategoriaManager()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    categoria = models.ForeignKey(
        'Categoria', 
        on_delete=models.CASCADE,
        related_name='categoria_libro'
    )
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('Titulo', max_length=50)
    publicado = models.DateField('Fecha de publicacion')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()

    objects = LibroManager()

    def __str__(self):
        return self.titulo