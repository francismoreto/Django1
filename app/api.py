from django.shortcuts import render
from ninja import NinjaAPI
from .models import Worker,Product,WorkerOutput
from .schema import WorkerSchema,codes


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
    Product.objects.create(
        item_code = data.item_code,
        part_no = data.part_no,
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
def create_process(request, procedure: codes):
    
    if new_procedure.completed:
        return("messsage":"Process installation complete")
    if new_procedure
    
       if new_procedure.current_step == 1:
        # Process user information
        if user_info:
            # Here you would save the user information
            new_procedure.current_step += 1  # Move to the next step
        else:
            return {"message": "User information is required to proceed."}

    elif new_procedure.current_step == 2:
        # Verify user information (this is just a placeholder)
        # Assume verification is successful
        new_procedure.current_step += 1  # Move to the next step

    elif new_procedure.current_step == 3:
        # Set up user preferences (this is just a placeholder)
        # Assume preferences are set successfully
        new_procedure.current_step += 1  # Move to the next step

    elif new_procedure.current_step == 4:
        # Complete onboarding
        new_procedure.completed = True
        new_procedure.current_step += 1  # Move to the next step (optional)

    # Save the onboarding process
    new_procedure.save()

    # Check if the onboarding is completed
    if new_procedure.completed:
        return {"message": "Onboarding completed successfully."}
    
    if new_procedure.completed:
        return("messsage":"Process installation complete")
    
    new_procedure = Product.object.create(
        process = {'process code': 'E151',
                 'process name': 'Winding wire'
         }
    )
    

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
    
   


