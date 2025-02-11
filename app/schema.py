from ninja import Schema

class WorkerSchema(Schema):
    Employee_id : str
    first_name : str
    last_name : str
    username : str

class Products(Schema):
    item_code : str
    Part_no : str
    process : str
    customer : str
    product_family : str

class Worker_out(Schema):
    lot_no : str
    current_status : str
    Out_data : str




    