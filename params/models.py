from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here. //


class MeasureUnit(models.Model):

    name = models.CharField(_('name'), max_length=20)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "MeasureUnit"
        verbose_name_plural = "MeasureUnits"

    def __str__(self):
        return "%s-%s" % (self.hi(), self.name)

    def hi(self):
        return "!Hi "


class Category(models.Model):

    name = models.CharField(_('name'), max_length=20)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(_('name'), max_length=20)
    code = models.CharField(max_length=10, null=True, blank=True)
    price = models.FloatField(default=0)
    measure_unit = models.ForeignKey(
        MeasureUnit, null=True, blank=True)  # related_name="measure_unit_set"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        unique_together = ('name',)

    def __str__(self):
        return "%s" % self.name
