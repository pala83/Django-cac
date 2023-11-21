from django.contrib import admin
from django.forms import ClearableFileInput
from .models import models
from .models import Cerveza, Proovedor, Cliente, Cualidad, IngresoInsumos

class ProovedorAdmin(admin.ModelAdmin):
    list_display = ( 'dni', 'nombre', 'apellido', 'empresa')
    list_editable = ('apellido', 'nombre', 'empresa')
    list_display_links = ['dni']

class InsumosAdmin(admin.ModelAdmin):
    list_display = ('proovedor', 'cerveza', 'cantidad', 'fecha')

class CervezaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': ClearableFileInput},
    }

admin.site.register(Cerveza, CervezaAdmin)
admin.site.register(Proovedor, ProovedorAdmin)
admin.site.register(Cliente)
admin.site.register(Cualidad)
admin.site.register(IngresoInsumos, InsumosAdmin)
# Register your models here.

