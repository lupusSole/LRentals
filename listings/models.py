from django.db import models

# Create your models here.

class Listing(models.Model):
    title = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=100)
    description = models.TextField()
    neighbourhood = models.CharField(max_length=25)
    image = models.ImageField(upload_to='lisitngs/images/')
    image2 = models.ImageField(upload_to='lisitngs/images/')
    image3 = models.ImageField(upload_to='lisitngs/images/')
    image4 = models.ImageField(upload_to='lisitngs/images/')
    image5 = models.ImageField(upload_to='lisitngs/images/')
    available = models.BooleanField(primary_key=False)
    dateAvailable = models.DateTimeField(null=True, blank=True )

    def __str__(self):
        return self.title


