import json
from apex_generator import ApexGenerator

with open('./start_session_schema.json', 'r') as f:
    json_schema = json.loads(f.read())
    ApexGenerator.from_json_schema(
        json_schema, 
        "StartSessionRes", 
        prefix="Cs", 
        output_path="./classes/")
