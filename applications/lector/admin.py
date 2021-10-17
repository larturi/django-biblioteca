from django.contrib import admin
from datetime import date

from .models import Lector, Prestamo
class LectorAdmin(admin.ModelAdmin):
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

class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        'lector',
        'libro',
        'fecha_prestamo',
        'fecha_devolucion',
        'devuelto',
    )

    search_fields = ('lector', 'libro')
    list_filter = ('devuelto',)

admin.site.register(Lector, LectorAdmin)
admin.site.register(Prestamo, PrestamoAdmin)
