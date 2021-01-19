import json
from apex_generator import ApexGenerator

with open('./schema/master.json', 'r') as f:
    json_schema = json.loads(f.read())
    ApexGenerator.from_json_schema(
        json_schema, 
        "Payload", 
        prefix="ComSys", 
        output_path="./classes/")