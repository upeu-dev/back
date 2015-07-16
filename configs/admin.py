from django.contrib import admin
from configs.models.JerarquiaAcad import JerarquiaAcad
from configs.models.Institucion import Institucion
from configs.models.Facultad import Facultad
from configs.models.Escuela import Escuela
from configs.models.Carrera import Carrera
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


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")


class CarreraAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")

admin.site.register(JerarquiaAcad, JerarquiaAcadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Carrera, CarreraAdmin)
