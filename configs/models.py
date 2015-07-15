# _*_ coding: utf-8 _*_
from django.db import models

# Create your models here.


class JerarquiaAcad(models.Model):

    institucion = models.ForeignKey('Institucion',  null=True, blank=True)
    parent = models.ForeignKey("self", null=True, blank=True)

    class Meta:
        verbose_name = "JerarquiaAcad"
        verbose_name_plural = "JerarquiaAcads"


class Institucion(models.Model):

    nombre = models.CharField(max_length=60)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    estructura_validada = models.BooleanField(default=False)

    jerarquia_acad = models.ForeignKey(
        JerarquiaAcad, related_name="institucion_set", null=True, blank=True)

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"

    def __str__(self):
        return self.abrev


class Facultad(models.Model):

    nombre = models.CharField(max_length=60)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    jerarquia_acad = models.ForeignKey(JerarquiaAcad, null=True, blank=True)

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

    def __str__(self):
        return self.abrev


class Escuela(models.Model):

    nombre = models.CharField(max_length=60)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    jerarquia_acad = models.ForeignKey(JerarquiaAcad, null=True, blank=True)

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

    def __str__(self):
        return self.abrev


class Carrera(models.Model):

    nombre = models.CharField(max_length=60)
    abrev = models.CharField(max_length=10, null=True, blank=True)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    jerarquia_acad = models.ForeignKey(JerarquiaAcad, null=True, blank=True)

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.abrev
