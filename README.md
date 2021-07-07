# JSON 2 Apex CLI

Python CLI for accomplishing the following:
* Converting a set of JSON objects into a JSON schema that describes the allowed elements for the given set of JSON objects
* Generating Apex classes based on a JSON schema

### Dependencies
* Python 3.x & pip
* Pipenv

### Installation
```
git clone https://github.com/hessbag/json2apexcli.git
cd ./json2apexcli && pip install -r requirements.txt
```

### Usage
##### Generate JSON Schema from JSON object files
Generates a JSON schema file based on a set of JSON objects provided as .json text files
```
./get-schema.py --targetdir ./json-objects/ --pattern '.*\.json' --outputpath ./master.json

--targetdir     The directory in which to search for files
--pattern       Python-style regex with which to match on filenames
--outputpath    Name for JSON schema file that will be created (as an output path)
```

##### Generate Apex classes from JSON schema file
Generates a hierarchy of classes based on a standard JSON schema file
```
Example:
./generate-schema.py --schemapath ./schema.json --classname Main --prefix NS --outputdir ./output/

--schemapath    Path of the JSON schema file to use for generating the classes
--prefix        String to prefix Apex classes with
--classname     Name of the parent class for the schema
--outputdir     Path of directory where classes should be written to
```