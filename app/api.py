from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Product,Worker_out
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

@api.post("/product")
def create_product(request, data: ProductSchema):
    
    valid_code = [choice[0] for choice in Product.PROCESS_CHOICE]

    if data.process not in valid_code:
        return{"error": f"Invalid process code: {data.process}. Must be one of {valid_code}."}
    
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

@api.post("/worker_out")
def create_output(request, data :WorkerOutputSchema):
    
    Worker_out.objects.create(
        lot_no = data.lot_no,
        current_status = data.current_status,
        output_data = data.output_data
    )
    
    
   


