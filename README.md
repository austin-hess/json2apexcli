# JSON-Apex

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
./json-apex.js get-schema --targetdir ./ --pattern 'Deposit_UC.*\.json' --outputpath master-schema.json

--targetdir     The directory in which to search for files
--pattern       Python-style regex with which to match on filenames
--outputpath    Name for JSON schema file that will be created
```

##### Generate Apex classes from JSON schema file
```
./json-apex.js generate-apex --schemafile ./master.json --prefix CS_ --classname Payload

--schemafile    Path of the JSON schema file to use for generating the classes
--prefix        String to prefix Apex classes with
--classname     Name of the parent class for the schema
```