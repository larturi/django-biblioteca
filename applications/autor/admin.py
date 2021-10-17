from django.contrib import admin
from datetime import date

from .models import Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'apellido',
        'nacionalidad',
        'fecha_nacimiento',
        'edad',
    )

    def edad(self, obj):
        today = date.today()
        return today.year - obj.fecha_nacimiento.year - ((today.month, today.day) < (obj.fecha_nacimiento.month, obj.fecha_nacimiento.day))

    search_fields = ('nombre', 'apellido')
    list_filter = ('nacionalidad',)

admin.site.register(Autor, AutorAdmin)
