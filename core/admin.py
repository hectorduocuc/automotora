from django.contrib import admin
from .models import Marca, Automovil
# Register your models here.


class AutomovilAdmin(admin.ModelAdmin):
    list_display = ('patente', 'marca', 'anio', 'modelo')
    search_fields = ('patente', 'modelo')
    list_filter = ('marca',)


admin.site.register(Marca)
admin.site.register(Automovil, AutomovilAdmin)