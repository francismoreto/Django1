from django.db import models
from ninja import Schema


class Worker(models.Model):
    employee_id = models.CharField(max_length=50, primary_key= True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=50)

class Product(models.Model):
    item_code = models.CharField (max_length=100)
    part_no = models.CharField(max_length=100)
    process = models.JSONField()
    customer = models.CharField(max_length=40)
    product_family = models.CharField(max_length=75)


class WorkerOutput(models.Model):
    lot_no = models.IntegerField()

    STATUS_CHOICE = [("ongoing","Ongoing"),("onhold","On Hold"),("finished","Finished")]

    current_status = models.CharField(max_length=20, choices= STATUS_CHOICE)
    output_data = models.JSONField()

    

    


    
