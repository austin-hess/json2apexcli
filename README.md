# JSON-Apex

## README is outdated - standby :sunglasses:

### Dependencies
* Python 3.x & pip
* Node & npm

### Installation
```
git clone https://bitbucket.org/nicoletbank/json-apex.git
cd ./json-apex
npm install
pip install -r requirements.txt
```

### Usage
##### Generate JSON Schema from JSON data files
```
./json-apex.js get-schema --targetdir <target-directory> --pattern <regular-expression> --outputpath <output-file-path>

--targetdir     The directory in which to search for files
--pattern       Python-style regex with which to match on filenames
					Example: .*\.json (All .json files)
--outputpath    Name for JSON schema file that will be created
```

##### Generate Apex classes from JSON schema file
```
Example:
./json-apex.js generate-apex --schemafile <schema-file-path> --prefix <class-prefix> --classname <class-name>

--schemafile    Path of the JSON schema file to use for generating the classes
--prefix        String to prefix Apex classes with
--classname     Name of the parent class for the schema
				Example: CS_Payload parent class would include references to other types defined in JSON schema
```