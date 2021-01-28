import apex

PRIMITIVES = ['string', 'number', 'integer', 'boolean']

class ApexGenerator:
    @staticmethod
    def from_json_schema(json_schema, name, *args, **kwargs):
        classes = []
        class_count = {}
        name = name
        prefix = "" if "prefix" not in kwargs else kwargs["prefix"]
        output_path = "./" if "output_path" not in kwargs else kwargs["output_path"]
        ApexGenerator.parse_json_schema(json_schema, prefix, name, classes, class_count)

        for _class in classes:
            filename = "{}{}".format(
                output_path + '/' if output_path[-1] != '/' else output_path,
                _class.name
            )
            with open("{}{}".format(filename, '.cls'), 'w') as f:
                f.write(_class.write())
            with open("{}{}".format(filename, '.cls-meta.xml'), 'w+') as f:
                f.write(apex.Class.write_meta())
    
    @staticmethod
    def parse_json_schema(schema, prefix, name, classes, class_count):
        curr_class = apex.Class("{}{}".format(prefix, name))

        for name, prop in schema['properties'].items():
            name = name if len(name+prefix) <= 40 else name[:39-len(prefix)]
            data_type = prop['type']

            if data_type in PRIMITIVES:
                print("Primitive: {} {}".format(data_type, name))
                data_type = 'decimal' if data_type == 'number' else data_type
                curr_class.members.append(apex.Member(name, data_type.capitalize()))

            elif data_type == 'array':
                print("Array: {} {}".format(data_type, name))

                props_to_process = []

                if prop['items'].get('anyOf') != None:
                    props_to_process.extend(prop['items']['anyOf'])
                else:
                    props_to_process.append(prop['items'])

                for i, p in enumerate(props_to_process):

                    if p['type'] in PRIMITIVES or isinstance(p['type'], list):
                        data_type = ''
                        if isinstance(p['type'], list):
                            data_type = p['type'][0]
                        else:
                            data_type = p['type']
                        data_type = 'decimal' if data_type == 'number' else data_type
                        curr_class.members.append(
                            apex.Member(name if i < 1 else name + "_" + str(i), "{}[]".format(data_type.capitalize()))
                        )

                    elif p['type'] == 'object':
                        var_name = ""
                        if name in class_count:
                            class_count[name] += 1
                            var_name = "{}{}".format(name, class_count[name])

                        else:
                            class_count[name] = 0
                            var_name = name
                        
                        ApexGenerator.parse_json_schema(p,prefix,var_name.capitalize(),classes,class_count)
                        curr_class.members.append(
                            apex.Member(name if i < 1 else name + "_" + str(i),"{}{}[]".format(prefix,var_name.capitalize()))
                        )

                    
            elif data_type == 'object':
                print("Object: {}".format(name))
                var_name = ""
                if name in class_count:
                    class_count[name] += 1
                    var_name = "{}{}".format(name, class_count[name])

                else:
                    class_count[name] = 0
                    var_name = name
                
                ApexGenerator.parse_json_schema(prop,prefix,var_name.capitalize(),classes,class_count)
                curr_class.members.append(
                    apex.Member(name, "{}{}".format(prefix,var_name.capitalize()))
                )
            
        classes.append(curr_class)


