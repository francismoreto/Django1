from django.contrib import admin
from .models import Worker, Products
# Register your models here.

class WorkerAdmin(admin.ModelAdmin):

    list_display = ('employee_id', 'first_name', 'last_name', 'username')

admin.site.register(Worker, WorkerAdmin)
admin.site.register(Products)

