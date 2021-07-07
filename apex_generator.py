import apex

PRIMITIVES = ['string', 'number', 'integer', 'boolean']
OUTPUT_PATH = './';

class Json2ApexGenerator:

    def __init__(self, json_schema):
        self.json_schema = json_schema
        self.output_path = OUTPUT_PATH

    def set_prefix(self, prefix):
        self.prefix = prefix

    def set_output_path(self, output_path):
        self.output_path = output_path

    def generate(self, name):
        self.classes = []
        self.class_count = {}
        self.parse_json_schema(self.json_schema, name)

        for _class in self.classes:
            filename = "{}{}".format(
                self.output_path + '/' if self.output_path[-1] != '/' else self.output_path,
                _class.name
            )
            with open("{}{}".format(filename, '.cls'), 'w') as f:
                f.write(_class.write())
            with open("{}{}".format(filename, '.cls-meta.xml'), 'w+') as f:
                f.write(apex.Class.write_meta())
    
    def parse_json_schema(self, schema, name):
        curr_class = apex.Class("{}{}".format(self.prefix, name))

        for prop_name, prop_data in schema['properties'].items():
            prop_name = self.trim_prop_name(prop_name)
            data_type = prop_data['type']

            if data_type in PRIMITIVES:
                data_type = 'decimal' if data_type == 'number' else data_type
                curr_class.members.append(apex.Member(prop_name, data_type.capitalize()))

            elif data_type == 'array':
                self.parse_array(curr_class, prop_data, prop_name)
                    
            elif data_type == 'object':
                self.parse_object(curr_class, prop_data, prop_name)

            elif isinstance(data_type, list):
                curr_class.members.append(
                    apex.Member(name, data_type[0].capitalize())
                )
            
        self.classes.append(curr_class)

    def parse_object(self, curr_class, prop_data, var_name):
        if var_name in self.class_count:
            self.class_count[var_name] += 1
            var_name = "{}{}".format(var_name, self.class_count[var_name])
        else:
            self.class_count[var_name] = 0
        
        self.parse_json_schema(prop_data, var_name.capitalize())
        curr_class.members.append(
            apex.Member(var_name, "{}{}".format(self.prefix, var_name.capitalize()))
        )
    
    def parse_primitive_array(self, curr_class, prop_type, prop_name):
        prop_type = 'decimal' if prop_type == 'number' else prop_type
        curr_class.members.append(
            apex.Member(prop_name, "{}[]".format(prop_type.capitalize()))
        )

    def parse_array(self, curr_class, prop_data, prop_name):
        if prop_data['items'].get('anyOf') != None:
            prop_data = prop_data['items']['anyOf'][0]
        else:
            prop_data = prop_data['items']

        prop_type = prop_data['type']

        if prop_type in PRIMITIVES:
            self.parse_primitive_array(curr_class, prop_type, prop_name)

        elif prop_type == 'object':
            self.parse_object(curr_class, prop_data, prop_name)
    
    def trim_prop_name(self, prop_name):
        return prop_name if len(prop_name + self.prefix) <= 40 else prop_name[:39 - len(self.prefix)]
