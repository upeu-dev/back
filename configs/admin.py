from django.contrib import admin
from .models import JerarquiaAcad, Institucion, Facultad, Escuela
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
    list_per_page = 2


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ("jerarquia_acad", "nombre", "abrev", "codigo")
    search_fields = ("nombre", "abrev", "codigo")
    list_per_page = 2

admin.site.register(JerarquiaAcad, JerarquiaAcadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Escuela, EscuelaAdmin)
