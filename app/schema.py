from ninja import Schema

class WorkerSchema(Schema):
    employee_id : str
    first_name : str
    last_name : str
    username : str

class ProductsSchema(Schema):
    item_code : str
    part_no : str
    process : str
    customer : str
    product_family : str

class WorkerOutputSchema(Schema):
    lot_no : str
    current_status : str
    output_data : str




    