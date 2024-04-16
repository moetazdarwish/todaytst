from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    age = models.DecimalField(max_digits=10,decimal_places=2,default=0.00, null=True, blank=True)
    nationalityID = models.PositiveIntegerField(null=True,blank=True,default=0)
    birthDate = models.DateField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)