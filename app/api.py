from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Products,Worker_out
from .schema import WorkerSchema, ProductsSchema


api = NinjaAPI()

@api.post("/worker")
def create_worker(request, data: WorkerSchema):
    Worker.objects.create(
        first_name = data.first_name,
        last_name = data.last_name,
        employee_id = data.employee_id,
        username = data.username)


