import datetime
from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
    
    def listar(self, kword):

        result = self.filter(
            titulo__icontains=kword        
        )

        return result

    def listar_trg(self, kword):

        if kword:
            # result = self.filter(
            #     titulo__trigram_similar=kword,      
            # )
            result = self.annotate(
                similarity=TrigramSimilarity('titulo', kword),
            ).filter(similarity__gt=0.3).order_by('-similarity')
            return result
        else:
            return self.all()

    def listar_by_fechas(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        result = self.filter(
            titulo__icontains=kword,
            publicado__range=(date1, date2)
        )

        return result

    def listar_by_categoria(self, categoria_id):
        return self.filter(
            categoria__id=categoria_id
        ).order_by('titulo')


    def add_autor_libro(self, libro_id, autor_id):
        libro = self.get(id=libro_id)
        libro.autores.add(autor_id)
        return libro


    def remove_autor_libro(self, libro_id, autor_id):
        libro = self.get(id=libro_id)
        libro.autores.remove(autor_id)
        return libro

    def cantidad_prestamos_libros(self):
        result = self.aggregate(
            num_prestamos = Count('libro_prestamo')
        )
        return result

    def libros_cantidad_prestamos(self):
        result = self.annotate(
            cant_prestamos = Count('libro_prestamo')
        )
        for r in result:    
            print(r, r.cant_prestamos)
        return result


class CategoriaManager(models.Manager):
    
    def categoria_by_autor(self, autor_id):
        result = self.filter(
            categoria_libro__autores__id=autor_id      
        ).distinct()

        return result

    def listar_categorias_libros(self):
        result = self.annotate(
            cant_libros = Count('categoria_libro')
        )
        return result
