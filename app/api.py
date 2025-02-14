from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Product,WorkerOutput
from .schema import WorkerSchema,codes,ProductSchema,WorkerOutputSchema


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
    



#Product input data
@api.post("/product")
def create_product(request, data: ProductSchema):   
       
    part_numbers = [
    {
        "part_no": "9900871000",
        "process_codes": ["process1", "process2", "process3", "process4", "process5", "process6"]
    },
    {
        "part_no": ["9901052019", "9901005015", "9901134012", "2346032","2346370","4FBA4411"],
        "process_codes": ["process1", "process2", "process3", "process4", "process5", "process6", "process7", "process8"]
    },
    {   "part_no": ["DTC12130D-B1", "2424110"],
        "process_codes": ["process1", "process2", "process3", "process4", "process5", "process6", "process7"]
    },
    {   "part_no": "2346360",
        "process_codes": ["process1", "process2", "process3", "process4", "process5"]

    },
    {
        "part_no": "BT65C202H01",
        "process_codes": ["process1", "process2", "process3", "process4", "process5", "process6", "process7", "process8","process9","process10","process11","process12","process13","process14"]

    }]
    #Process code equivalent on process name
    process_code_mapping = {
        "process_ code": " E151", "process_name": "Winding wire",
        "E203": "1st Cutting Wire",
        "E208": "Turn, inductance",
        "E205": "1st peeling",
        "E201": "1st soldering",
        "E209": "Adhering pedestal, coil",
        "E324": "Drying Adhesive",
        "E204": "Intermediate inductance",
        "E124": "Adhering pedestal, drying",
        "E515": "Impulse",
        "E210": "Inseting white tubes",
        "E211": "Inserting black tubes",
        "E333": "Crimping terminal",
        "E345": "Terminal soldering",
        "E334": "Heat shrinking",
        "E346": "Terminal coil forming",
        "E508": "Final electrical inspection (L/Impulse)",
        "E611": "Appearance",
        "E621": "Jig for checking terminal",
        "E321": "Adhering pedestal(substrate)",
        "E200": "Wire marking",
        "E325": "Coil taping"
    }
    process = []

    # Find the part number in the part_numbers list
    for part in part_numbers:
        if data.part_no in part["part_no"] if isinstance(part["part_no"], list) else [part["part_no"]]:
            # Populate the process list with code and name
            # Populate the process list with code and name
            process = [{"process_code": code, "process_name": process_code_mapping.get(code, "Unknown Process")} for code in part["process_codes"]]

            break
    else:
        return {"message": "Part number not found."}
    
   # Create the product object
    Product.objects.create(
        item_code=data.item_code,
        part_no=data.part_no,
        process=process,  # Use the found process codes with names
        customer=data.customer,
        product_family=data.product_family,
    )

    return {
        "message": "Product successfully stored",
        "item_code": data.item_code,
        "part_no": data.part_no,
        "process": process,
        "customer": data.customer,
        "product_family": data.product_family
    }

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
    
   


