from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

class resourceMascota(resources.ModelResource):
    class Meta:
        model = Mascota

class AdminMascota(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['edad','raza','nombre']
    resource_class = resourceMascota

admin.site.register(Mascota, AdminMascota)

##

class resourceCliente(resources.ModelResource):
    class Meta:
        model = Cliente

class AdminCliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['edad', 'nombre','fk_Mascota']
    resource_class = resourceCliente

admin.site.register(Cliente, AdminCliente)

##

class resourceCita(resources.ModelResource):
    class Meta:
        model = Cita

class AdminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha']
    list_display = ['fecha', 'fk_Cliente', 'fk_Mascota']
    resource_class = resourceCita

admin.site.register(Cita, AdminCita)