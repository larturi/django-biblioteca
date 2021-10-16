from django.db import models
from django.db.models.signals import post_save

from PIL import Image

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
    stock = models.PositiveIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo',]

    def __str__(self):
        return self.titulo

def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=90, optimize=True)


post_save.connect(optimize_image, sender=Libro)