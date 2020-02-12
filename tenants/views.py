from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TenantForm
from .models import Tenant
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupTenant(req):
    if req.method == 'GET':
         return render(req, 'tenants/signuptenant.html', {'form': UserCreationForm()})
    else:
        # create new user
        if req.POST['password1']== req.POST['password2']:
            try:
                user = User.objects.create_user(req.POST['username'], password=req.POST['password1'])
                user.save()
                login(req, user)
                return redirect('tenantarea')

            except IntegrityError:
                 return render(req, 'tenants/signuptenant.html', {'form': UserCreationForm(), 'error': 'Username has been take, please choose a new username'})    
        else:
             return render(req, 'tenants/signuptenant.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})
@login_required
def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')
def loginuser(req):
         if req.method == 'GET':
           return render(req, 'tenants/login.html', {'form': AuthenticationForm()})
         else:
           user = authenticate(req, username=req.POST['username'], password=req.POST['password'])
           if user is None:
               return render(req, 'tenants/login.html', {'form': AuthenticationForm(), 'error': "Username And Password Did Not Match"})
           else:
               login(req, user)
               return redirect('tenantarea')



@login_required       
def tenantarea(req):
    tenants = Tenant.objects.filter(tenant = req.user)
    return render(req, 'tenants/tenantarea.html', {'tenants': tenants})
@login_required
def viewtenant(req, tenant_pk):
    tenant = get_object_or_404(Tenant, pk=tenant_pk, tenant=req.user)
    if req.method == 'GET':
        form = TenantForm(instance=tenant)
        return render(req, 'tenants/tenant.html', {'tenant': tenant, 'form': form})
    else:
        try:
            form = TenantForm(req.POST, instance=tenant)
            form.save()
            return redirect('tenantarea')
        except ValueError:
            return render(req, 'tenants/tenant.html', {'tenant': tenant, 'form': form, 'error': "Bad Info"})


   
@login_required
def createprofile(req):
    if req.method == "GET":
         return render(req, 'tenants/create.html', {'form': TenantForm})
    else:
        try:
              form = TenantForm(req.POST)
              newTenant = form.save(commit=False)
              newTenant.tenant = req.user
              newTenant.save()
              return redirect('home')
        except ValueError:
             return render(req, 'tenants/create.html', {'form': TenantForm, 'error': "Error"})
      

   



   

