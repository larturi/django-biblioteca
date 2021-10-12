from django.db import models
from django.db.models import Q
class AutorManager(models.Manager):
    
    def buscar_autor_nombre(self, kword):

        result = self.filter(
            nombre__icontains=kword
        )

        return result

    def buscar_autor_apenom(self, kword):

        result = self.filter(
           Q(nombre__icontains = kword) | Q(apellido__icontains = kword)
        )

        return result

    