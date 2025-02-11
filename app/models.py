from django.db import models
from ninja import Schema


class Worker(models.Model):
    Employee_id = models.CharField(max_length=50)
    first_name = models.CharField(max_lenght=25)
    last_name = models.CharField(max_length=20)
    username = models

class lot(models.Model):
    Worker = models.CharField (max_length=100)
    lot_no = models.IntegerField
    Part_no = models.CharField(max_length=100)
    Process = models.CharField(max_length=100)
    Gd_qty = models.IntegerField
    Ng_qty = models.IntegerField
    Status = models.CharField(max_length=10)

class Process(models.Model):
    Worker = models.CharField(max_length=100)
    Process = models.CharField(max_length=4)
    Gd_qty = models.IntegerField
    Ng_qty = models.IntegerField
    Status = models.CharField(max_length=9)

    
