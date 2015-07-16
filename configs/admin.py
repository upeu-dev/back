from django.contrib import admin
<<<<<<< HEAD
from configs.models.JerarquiaAcad import JerarquiaAcad
from configs.models.Institucion import Institucion
from configs.models.Facultad import Facultad
from configs.models.Escuela import Escuela
from configs.models.Carrera import Carrera
=======
from .models import JerarquiaAcad, Institucion, Facultad, Escuela
>>>>>>> 40a7efb65ed2708c6662d52a4bbe075ff48ccfa1
# Register your models here.


class JerarquiaAcadAdmin(admin.ModelAdmin):
    list_display = ("tipo", "institucion", "parent")


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
    list_per_page = 2


class FacultadAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
<<<<<<< HEAD
=======
    list_per_page = 2
>>>>>>> 40a7efb65ed2708c6662d52a4bbe075ff48ccfa1


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
<<<<<<< HEAD


class CarreraAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
=======
    list_per_page = 2
>>>>>>> 40a7efb65ed2708c6662d52a4bbe075ff48ccfa1

admin.site.register(JerarquiaAcad, JerarquiaAcadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Escuela, EscuelaAdmin)
<<<<<<< HEAD
admin.site.register(Carrera, CarreraAdmin)
=======
>>>>>>> 40a7efb65ed2708c6662d52a4bbe075ff48ccfa1
