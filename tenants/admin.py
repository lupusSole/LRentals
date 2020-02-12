from django.contrib import admin
from .models import Tenant

class TenantAdmin(admin.ModelAdmin):
    readonly_fields = ('profileCreated',)


admin.site.register(Tenant, TenantAdmin)