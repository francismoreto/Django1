from django.contrib import admin
from .models import Worker, Product
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):

    list_display = ('employee_id', 'first_name', 'last_name', 'username')

class ProductAdmin(admin.ModelAdmin):

    list_display = ('item_code', 'part_no', 'process', 'customer', 'product_family')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Product, ProductAdmin)

