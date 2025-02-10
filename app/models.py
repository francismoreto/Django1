from django.db import models
from ninja import Schema


class Employee(models.Model):
    Name = models.CharField(max_length=50)
    Employee_no = models.CharField(max_length=50)
    Section = models.CharField(max_length=50)

class lot_no(models.Model):
    Employee_no = models.foreignkey
    
