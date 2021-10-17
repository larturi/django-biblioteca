from django.db import models
from django.db.models.functions import Lower
from django.db.models import Count

class PrestamoManager(models.Manager):
    
    def libros_cantidad_lectores(self, id_libro):

        result = self.filter(
            libro__id=id_libro
        ).aggregate(
            cant_lectores = Count('lector')
        )

        return result

    def libros_cantidad_prestamos(self):
        result = self.values(
            'libro'
        ).annotate(
            cant_prestamos = Count('libro'),
            titulo = Lower('libro__titulo')
        )
        for r in result:    
            print(r, r['cant_prestamos'])
        return result
