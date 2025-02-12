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
   
    PROCESS_CHOICE = (
    ('Step1', 'E151'),
    ('Step2', 'E203'),
    ('Step3', 'E208'),
    ('Step4', 'E205'),
    ('Step5', 'E201'),
)
    process = models.CharField(max_length=50, choices= PROCESS_CHOICE)
    customer = models.CharField(max_length=40)
    product_family = models.CharField(max_length=75)

class Worker_out(models.Model):
    lot_no = models.IntegerField
    current_status = models.CharField(max_length=20)
    output_data = models.JSONField()

    


    
