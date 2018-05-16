from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'priceold','decrease', 'stock', 'available', 'created', 'updated', 'new','hot']
    list_filter = ['available', 'created', 'updated', 'category', 'new', 'hot']
    list_editable = ['price','priceold','decrease', 'stock', 'available', 'new', 'hot']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
