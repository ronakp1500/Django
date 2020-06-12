from django.db import models

#Create your models here.

class Boot_Table(models.Model):
    Name=models.CharField(max_length=20,blank=False)
    ID=models.CharField(max_length=20,primary_key=True)
    Contact=models.IntegerField(default="")
    Address=models.CharField(max_length=100)


    