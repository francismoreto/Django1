from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Product,WorkerOutput
from .schema import WorkerSchema,ProductSchema,WorkerOutputSchema


api = NinjaAPI()

@api.post("/worker")
def create_worker(request, data: WorkerSchema):
    if Worker.objects.filter(employee_id=data.employee_id).exists():
        return {"error": "Employee already exist"}
    try:
        new_worker=Worker.objects.create(
        first_name = data.first_name,
        last_name = data.last_name,
        employee_id = data.employee_id,
        username = data.username)
        return {"message": "Worker created successfully",
            "first_name": data.first_name,
            "last_name": data.last_name,
            "employee_id": data.employee_id,
            "username": data.username
        }
    except Exception as e:
        return {"error": str(e)}


@api.post("/process")
def create_process(request, data: process )

@api.post("/product")
def create_product(request, data: ProductSchema):   
    Product.objects.create(
        item_code = data.item_code,
        part_no = data.part_no,
        process = data.process,
        customer = data.customer,
        product_family = data.product_family
        )

    return {"message": "Product successfully stored",
            "item_code": data.item_code,
            "part_no": data.part_no,
            "process": data.process,
            "customer": data.customer,
            "product_family": data.product_family
        }

@api.post("/")

@api.post("/worker-output")
def create_output(request, data :WorkerOutputSchema):
    

    WorkerOutput.objects.create(
        lot_no = data.lot_no,
        current_status = data.current_status,
        output_data = data.output_data
    )
    return {"message": "Data added successfully",
            "lot_no": data.lot_no,
            "current_status": data.current_status,
            "output_data": data.output_data,
        }
    
   


