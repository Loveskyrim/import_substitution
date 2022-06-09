from django.contrib import admin
from .models import organisation, product


class OrganisationAdmin(admin.ModelAdmin):
    "Админка организации"""
    fields = ('OS_name', 'id_bulletin', 'url_bulletin')


class ProductAdmin(admin.ModelAdmin):
    "Админка продукта"""
    fields = ('OS_name', 'id_bulletin', 'url_bulletin', 'bulletin_author', 'status')


admin.site.register(organisation, OrganisationAdmin)
admin.site.register(product, ProductAdmin)

