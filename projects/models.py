from django.db import models
from clients.models import Client
from contacts.models import Contact

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    location = models.TextField()
    company = models.ForeignKey(Client, on_delete=models.CASCADE)
    manager = models.ForeignKey(Contact, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
