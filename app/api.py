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
    part_numbers = [
        {"part_no": "9900871000", "process_codes_length": 6},
        {"part_no": ["9901052019", "9901005015", "9901134012", "2346032", "2346370", "4FBA4411"], "process_codes_length": 8},
        {"part_no": ["DTC12130D-B1", "2424110"], "process_codes_length": 7},
        {"part_no": "2346360", "process_codes_length": 5},
        {"part_no": "BT65C202H01", "process_codes_length": 22}
    ]

    process_code_mapping = {
        "E151": "Winding wire",
        "E203": "1st Cutting Wire",
        "E208": "Turn, inductance",
        "E205": "1st peeling",
        "E201": "1st soldering",
        "E209": "Adhering pedestal, coil",
        "E324": "Drying Adhesive",
        "E204": "Intermediate inductance",
        "E124": "Adhering pedestal, drying",
        "E515": "Impulse",
        "E210": "Inserting white tubes",
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

    # Find the part number in the part_numbers list
    part_found = False
    process_codes_length = 0
    for part in part_numbers:
        part_no_list = part["part_no"] if isinstance(part["part_no"], list) else [part["part_no"]]
        if data.part_no in part_no_list:
            part_found = True
            process_codes_length = part["process_codes_length"]
            break

    if not part_found:
        return {"message": "Part number not found."}

    # Validate process codes from the incoming data
    process_codes_to_validate = []

    if isinstance(data.process, list):
        for item in data.process:
            if isinstance(item, dict):
                process_code = item.get('process_code')
                if process_code:
                    process_codes_to_validate.append(process_code)
            elif isinstance(item, str):
                process_codes_to_validate.append(item)
    else:
        return {"message": "Invalid process format. Expected a list of dictionaries or strings."}

    # Check if the number of process codes matches the required length
    if len(process_codes_to_validate) != process_codes_length:
        return {"message": f"Invalid number of process codes. Expected {process_codes_length}, got {len(process_codes_to_validate)}"}

    # Check for invalid process codes
    invalid_process_codes = [code for code in process_codes_to_validate if code not in process_code_mapping]
    if invalid_process_codes:
        return {"message": f"Invalid process codes: {', '.join(invalid_process_codes)}"}

    # Populate the process list with code and name
    process = [{"process_code": code, "process_name": process_code_mapping[code]} for code in process_codes_to_validate]

    try:
        Product.objects.create(
            item_code=data.item_code,
            part_no=data.part_no,
            process=process,
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
    
   



