from django.contrib import admin
from .models import organisation, product, okved


class OrganisationAdmin(admin.ModelAdmin):
    "Админка организации"""
    list_display = ('organisation_name', 'organisation_okved', 'organisation_category', 'organisation_sanctions')
    list_filter = ('organisation_name', 'organisation_okved', 'organisation_category', 'organisation_sanctions')
    search_fields = ('organisation_name', 'organisation_okved', 'organisation_category')
    prepopulated_fields = {'slug': ('organisation_name',)}
    ordering = ['organisation_name', 'organisation_category']


class ProductAdmin(admin.ModelAdmin):
    "Админка продукта"""
    list_display = ('product_name', 'product_tags', 'product_info', 'product_sanctions_import', 'product_sanctions_export')
    list_filter = ('product_name', 'product_tags', 'product_sanctions_import', 'product_sanctions_export')
    search_fields = ('product_name', 'product_tags')
    prepopulated_fields = {'slug': ('product_name',)}
    ordering = ['product_name']

class OkvedAdmin(admin.ModelAdmin):
    "Админка номера ОКВЭД"""
    list_display = ('id_okved', 'name', 'description')
    list_filter = ('id_okved', 'name', 'description')
    search_fields = ('id_okved', 'name', 'description')
    ordering = ['id_okved']


admin.site.register(organisation, OrganisationAdmin)
admin.site.register(product, ProductAdmin)
admin.site.register(okved, OkvedAdmin)


