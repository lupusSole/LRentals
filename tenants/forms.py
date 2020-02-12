from django.forms import ModelForm
from .models import Tenant

class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['firstName', 'lastName', 'email', 'phone', 'address']