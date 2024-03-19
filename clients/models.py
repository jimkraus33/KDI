from django.db import models
from contacts.models import Contact

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=128)
    location = models.TextField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    contacts = models.ManyToManyField(Contact)
    date_created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    

