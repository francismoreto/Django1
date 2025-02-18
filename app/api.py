from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Product,WorkerOutput
from .schema import WorkerSchema,ProductSchema,WorkerOutputSchema


api = NinjaAPI()


#Worker input data
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

    process_code_mapping = [
        {"E151": "Winding wire"},
        {"E203": "1st Cutting Wire"},
        {"E208": "Turn, inductance"},
        {"E205": "1st peeling"},
        {"E201": "1st soldering"},
        {"E209": "Adhering pedestal, coil"},
        {"E324": "Drying Adhesive"},
        {"E204": "Intermediate inductance"},
        {"E124": "Adhering pedestal, drying"},
        {"E515": "Impulse"},
        {"E210": "Inserting white tubes"},
        {"E211": "Inserting black tubes"},
        {"E333": "Crimping terminal"},
        {"E345": "Terminal soldering"},
        {"E334": "Heat shrinking"},
        {"E346": "Terminal coil forming"},
        {"E508": "Final electrical inspection (L/Impulse)"},
        {"E611": "Appearance"},
        {"E621": "Jig for checking terminal"},
        {"E321": "Adhering pedestal(substrate)"},
        {"E200": "Wire marking"},
        {"E325": "Coil taping"}
    ]


    #if process_code_mapping["E151"]:
        #return {"message":"E151 has value"}

    # Validate process codes from the incoming data
    #process_codes_to_validate = []

    # Check for invalid process codes
    #invalid_process_codes = [code for code in process_codes_to_validate if code not in process_code_mapping]
    #if invalid_process_codes:
        #return {"message": f"Invalid process codes: {', '.join(invalid_process_codes)}"}

    # Populate the process list with code and name
    # process = [{"process_code": code, "process_name": process_code_mapping[code]} for code in process_codes_to_validate]

    try:
        Product.objects.create(
            item_code=data.item_code,
            part_no=data.part_no,
            process= data.process,
            customer=data.customer,
            product_family=data.product_family,
        )
        return {
            "message": "Product successfully stored",
            "item_code": data.item_code,
            "part_no": data.part_no,
            "process": data.process,
            "customer": data.customer,
            "product_family": data.product_family
        }
    except Exception as e:
        return {"message": f"Error creating product: {str(e)}"}


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
    
   



