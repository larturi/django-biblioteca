from django.contrib import admin

from .models import Libro, Categoria
class LibroAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'categoria',
        'autores_list',
        'publicado',
        'visitas',
        'stock',
    )

    def autores_list(self, obj):
        return "\n".join([autor.nombre + ' ' + autor.apellido for autor in obj.autores.all()])

    search_fields = ('titulo', 'autores')
    list_filter = ('categoria', 'autores')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )

    search_fields = ('nombre',)

admin.site.register(Libro, LibroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
