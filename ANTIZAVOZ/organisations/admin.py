from django.contrib import admin
from .models import organisation, product


class OrganisationAdmin(admin.ModelAdmin):
    "Админка организации"""
    fields = ('id_organisation', 'organisation_okved', 'organisation_category', 
        'organisation_description', 'organisation_principal', 'organisation_link', 'organisation_sanctions')


class ProductAdmin(admin.ModelAdmin):
    "Админка продукта"""
    fields = ('product_name', 'product_tags', 'product_info', 'product_sanctions_import', 'product_sanctions_export')


admin.site.register(organisation, OrganisationAdmin)
admin.site.register(product, ProductAdmin)

