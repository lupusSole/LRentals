from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tenant(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    movedIn = models.DateTimeField(null=True, blank=True )
    profileCreated = models.DateTimeField(auto_now_add=True)
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address


