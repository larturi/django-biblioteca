from django.db import models

class AutorManager(models.Manager):
    
    def listar_autores(self):
        return self.all()