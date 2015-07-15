from django.contrib import admin
from params.models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    list_per_page = 2


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code",)
    list_per_page = 2

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
