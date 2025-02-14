from ninja import Schema
from datetime import datetime
from typing import List

class WorkerSchema(Schema):
    employee_id : str
    first_name : str
    last_name : str
    username : str

class codes(Schema):
    process_code: str
    process_name: str


class ProductSchema(Schema):
    item_code : str
    part_no : str
    process : List[codes]
    customer : str
    product_family : str


class StaticData(Schema):
    employee_id: str
    item_code : str
    process_code: str
    process_name: str

class DynamicData(Schema):
    lot_quantity: int
    good_quantity: int
    defect_quantity: int

class timestamp():
    datetime_start: datetime
    datetime_end: datetime    
class WorkerOutputSchema(Schema):
    lot_no : int
    current_status : str
    output_data : str




    