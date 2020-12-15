const { ApexClass, ApexClassProperty } = require('./apex');
const { capitalizeFirstChar } = require('./utils');
const keywords = require('./keywords');
const fs = require('fs');

function parseObject(object, prefix, objectName, primitives, existingTypes, classes) {

    var currentClass = new ApexClass(`${prefix}${objectName}`);

    for (var propertyName in object.properties) {

        let propertyType = capitalizeFirstChar(propertyName);

        if (existingTypes.includes(propertyType)) {

            addToClass(currentClass, propertyType, propertyName);
        }
        else {
            let propertyObj = object.properties[propertyName];
            
            if (primitives.includes(propertyObj.type)) {

                let primitiveTypeName =  capitalizeFirstChar(propertyObj.type);
                if (primitiveTypeName == 'Number') primitiveTypeName = 'Decimal';
               
                addToClass(currentClass, primitiveTypeName, propertyName);
            }
            if (propertyObj.type == 'object') {

                let type = parseObject(propertyObj, prefix, propertyType, primitives,existingTypes, classes);

                addToClass(currentClass, type, propertyName);
            }
            if (propertyObj.type == 'array') {

                if (primitives.includes(propertyObj.items.type)) {

                    let primitiveTypeName =  capitalizeFirstChar(propertyObj.items.type);
                    if (primitiveTypeName == 'Number') primitiveTypeName = 'Decimal';
                    addToClass(currentClass, `${primitiveTypeName}[]`, propertyName);
                }
                else if (propertyObj.items.type == 'object') {

                    let type = parseObject(propertyObj.items, prefix, propertyType, primitives, existingTypes, classes);
                    addToClass(currentClass, `${type}[]`, propertyName);
                }
            }

        }
    }

    classes.push(currentClass);
    existingTypes.push(currentClass.name);

    return currentClass.name;
}

function addToClass(cls, propertyType, propertyName) {
    propertyName = keywords.includes(propertyName) ? `${propertyName}_x` : propertyName;
    cls.withProp(new ApexClassProperty(propertyType, propertyName));
}

module.exports = (schemaPath, prefix, requestClassName, outputDir) => {

    const data = JSON.parse(fs.readFileSync(schemaPath, 'utf-8'));

    var primitives = ['string', 'number', 'integer', 'boolean'];
    var classes = [];
    var existingTypes = [];

    parseObject(data, prefix, requestClassName, primitives, existingTypes, classes);
    
    let metadataFileContent = '<?xml version="1.0" encoding="UTF-8"?>\n<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">\n\t<apiVersion>49.0</apiVersion>\n\t<status>Active</status>\n</ApexClass>';
    
    classes.forEach(currentClass => {
        let filename = `${currentClass.name}.cls`;
        fs.writeFileSync(`${outputDir}/${filename}`, currentClass.generate(), { flag: 'w'});
        fs.writeFileSync(`${outputDir}/${currentClass.name}.cls-meta.xml`,metadataFileContent, {flag: 'w'});
    });
}

