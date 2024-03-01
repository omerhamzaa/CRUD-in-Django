from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length= 20)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    phone = models.IntegerField()
