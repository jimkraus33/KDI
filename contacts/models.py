from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)   
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
