from django.contrib.admin import ModelAdmin, register

from api.models import Client, Organization, Bills


@register(Client)
class ClientAdmin(ModelAdmin):
    lust_display = ('name')
    list_filter = ('name', )


@register(Organization)
class OrganizationAdmin(ModelAdmin):
    pass


@register(Bills)
class BillsAdmin(ModelAdmin):
    pass
