from django.contrib import admin

from product import models

class ProductColorInline(admin.TabularInline):
    model = models.ProductColour
    extra = 1


class ProductComponentsInline(admin.TabularInline):
    model = models.ProductComponents
    extra = 1


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand')
    inlines = [ProductColorInline, ProductComponentsInline, ProductImageInline]


@admin.register(models.CategoryProduct)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.BrandProduct)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
