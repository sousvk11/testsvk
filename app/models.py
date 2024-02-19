from django.db import models

# Create your models here.
class usr_reg(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    passwd=models.CharField(max_length=100)