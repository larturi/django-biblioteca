import datetime
from django.db import models

class LibroManager(models.Manager):
    
    def listar(self, kword):

        result = self.filter(
            titulo__icontains=kword        
        )

        return result

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