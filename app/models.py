from django.db import models
from ninja import Schema


class Worker(models.Model):
    Employee_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)

class Products(models.Model):
    item_code = models.CharField (max_length=100)
    Part_no = models.CharField(max_length=100)
    process = models.CharField(max_length=100)
    customer = models.CharField(max_length=40)
    product_family = models.CharField(max_length=75)

class Worker_out(models.Model):
    lot_no = models.IntegerField(max_length=100)
    current_status = models.CharField(max_length=20)
    Out_data = models.JSONField()

    


    
