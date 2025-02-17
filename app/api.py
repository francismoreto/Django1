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
        {
            "part_no": "9900871000",
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209"]
        },
        {
            "part_no": ["9901052019", "9901005015", "DTC12130D-B1"],
            "process_codes": ["E151", "E203", "E208", "E200", "E205", "E201", "E209", "E324"]
        },
        {
            "part_no": "9901134012",
            "process_codes": ["E151", "E203", "E200", "E208", "E205", "E201", "E209", "E324"]
        },
        {
            "part_no": "2424110",
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209", "E324"]
        },
        {
            "part_no": "BT65C202H01",
            "process_codes": ["E151", "E203", "E208", "E205", "E210", "E211", "E333", "E345", "E334", "E346", "E508", "E515", "E611", "E621"]
        },
        {
            "part_no": "PRA2992-2-7",
            "process_codes": ["E151", "E203", "E204", "E205", "E201", "E124"]
        },
        {
            "part_no": ["2346032", "2346370", "2346360"],
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E209", "E324", "E325"]
        },
        {
            "part_no": "4FBA4411",
            "process_codes": ["E151", "E203", "E208", "E205", "E201", "E321", "E323", "E324"]
        },
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

    part_found = False
    process_codes = []
    
    for part in part_numbers:
        part_no_list = part["part_no"] if isinstance(part["part_no"], list) else [part["part_no"]]
        
        if data.part_no in part_no_list:
            part_found = True
            process_codes = part["process_codes"]
            break

    if not part_found:
        if data.action == "add":
       
            invalid_process_codes = [code for code in data.process_codes if code not in process_code_mapping]
        if invalid_process_codes:
            invalid_process_codes_str = [str(code) for code in invalid_process_codes]
            return {"message": f"Invalid process codes: {', '.join(invalid_process_codes_str)}"}
    process_codes_to_validate = []

    if isinstance(data.process, list):
        for item in data.process:
            if isinstance(item, dict):
                process_code = item.get('process_code')
                if process_code:
                    process_codes_to_validate.append(process_code)
            else:
                process_codes_to_validate.append(item)

    invalid_process_codes = [code for code in process_codes_to_validate if code not in process_code_mapping]
    if invalid_process_codes:
        invalid_process_codes_str = [str(code) for code in invalid_process_codes]
        return {"message": f"Invalid process codes: {', '.join(invalid_process_codes_str)}"}

    process = [{"process_code": code, "process_name": process_code_mapping[code]} for code in process_codes]

    try:
        new_part = {
                "part_no": data.part_no,
                "process_codes": data.process_codes
            }
        part_numbers.append(new_part)
        Product.objects.create(
            item_code=data.item_code,
            part_no=data.part_no,
            process=[
                    {"process_code": code, "process_name": process_code_mapping[code]}
                    for code in data.process_codes
                ],
            customer=data.customer,
            product_family=data.product_family
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
    
   


