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
    



@api.post("/product")
def create_product(request, data: ProductSchema):   
       
    part_numbers = [
        {
            "part_no": "9900871000",
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209"]
        },
        {
            "part_no": ["9901052019", "9901005015", "9901134012", "2346032", "2346370", "4FBA4411"],
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209", "E324", "E204"]
        },
        {
            "part_no": ["DTC12130D-B1", "2424110"],
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209", "E324"]
        },
        {
            "part_no": "2346360",
            "process_codes": ["E151", "E203", "E208", "E205", "E201"]
        },
        {
            "part_no": "BT65C202H01",
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209", "E324", "E204", "E515", "E210", "E211", "E333", "E345", "E334", "E346", "E508", "E611", "E621", "E321", "E200", "E325"]
        }
    ]

    # Process code equivalent on process name
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
    process_codes = []
    for part in part_numbers:
        part_no_list = part["part_no"] if isinstance(part["part_no"], list) else [part["part_no"]]
        
        if data.part_no in part_no_list:
            part_found = True
            process_codes = part["process_codes"]  # Get the corresponding process codes
            break

    if not part_found:
        return {"message": "Part number not found."}, 404  # Return a tuple with status code 404

    # Validate process codes from the incoming data
    # If `data.process` is a list of dictionaries, we need to extract the 'process_code' field first
    process_codes_to_validate = []

    if isinstance(data.process, list):
        for item in data.process:
            if isinstance(item, dict):
                # Extract process_code from the dictionary
                process_code = item.get('process_code')
                if process_code:
                    process_codes_to_validate.append(process_code)
            else:
                # If it's a direct code, just add it
                process_codes_to_validate.append(item)

    # Now check for invalid process codes
    invalid_process_codes = [code for code in process_codes_to_validate if code not in process_code_mapping]
    if invalid_process_codes:
        # Ensure all invalid process codes are strings before joining them
        invalid_process_codes_str = [str(code) for code in invalid_process_codes]
        return {"message": f"Invalid process codes: {', '.join(invalid_process_codes_str)}"}, 400  # Return a tuple with status code 400

    # Populate the process list with code and name
    process = [{"process_code": code, "process_name": process_code_mapping[code]} for code in process_codes_to_validate]

    # Create the product object
    Product.objects.create(
        item_code=data.item_code,
        part_no=data.part_no,
        process=process,  # Use the validated process codes with names
        customer=data.customer,
        product_family=data.product_family,
    )

    # Return the success message and status code 201
    return {
        "message": "Product successfully stored",
        "item_code": data.item_code,
        "part_no": data.part_no,
        "process": process,
        "customer": data.customer,
        "product_family": data.product_family
    }, 201  # Return a tuple with status code 201


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
    
   


