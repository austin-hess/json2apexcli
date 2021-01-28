# JSON-Schema-to-Apex

A tool for merging JSON files into a single schema and a tool for generating Apex code from a JSON schema

### Dependencies
* Python 3.x & pip
* Pipenv

### Installation
```
git clone https://bitbucket.org/nicoletbank/json-schema-to-apex.git
cd ./json-schema-to-apex
pipenv install
```

### Usage
##### Generate JSON Schema from JSON data files
```
./get-schema.py --targetdir ./ --pattern '.*\.json' --outputpath ./master.json

--targetdir     The directory in which to search for files
--pattern       Python-style regex with which to match on filenames
					Example: .*\.json (All .json files)
--outputpath    Name for JSON schema file that will be created
```

##### Generate Apex classes from JSON schema file
```
Example:
./generate-schema.py --schemapath ./schema.json --classname Main --prefix NS --outputdir ./output/

--schemapath    Path of the JSON schema file to use for generating the classes
--prefix        String to prefix Apex classes with
--classname     Name of the parent class for the schema
--outputdir     Path of directory where classes should be written to
```