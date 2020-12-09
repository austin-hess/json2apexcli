const { ApexClass, ApexClassProperty } = require('./apex');
const fs = require('fs');

const data = JSON.parse(fs.readFileSync('./master-schema.json', 'utf-8'));

function parseObject(obj, prefix, objName, typeRefs, primitiveTypes, classes) {

    let cls = new ApexClass(prefix + objName);

    for (var propName in obj.properties) {

        let propType = propName.charAt(0).toUpperCase() + propName.slice(1);

        if (typeRefs.includes(propType)) {
            let prop = new ApexClassProperty(propType, propName);
            cls.withProp(prop);
        }
        else {
            let prop = obj.properties[propName];
            
            if (primitiveTypes.includes(prop.type)) {
                let varType =  prop.type.charAt(0).toUpperCase() + prop.type.slice(1);

                if (varType == 'Number') varType = 'Decimal';
                
                cls.withProp(new ApexClassProperty(varType, propName));
            }
            if (prop.type == 'object') {
                parseObject(prop, prefix, propType, typeRefs, primitiveTypes, classes);
                cls.withProp(new ApexClassProperty(propType,propName));
            }
            if (prop.type == 'array') {
                if (primitiveTypes.includes(prop.items.type)) {
                    let varType =  prop.items.type.charAt(0).toUpperCase() + prop.items.type.slice(1);
                    cls.withProp(new ApexClassProperty(varType + '[]', propName));
                }
                else if (prop.items.type == 'object') {
                    parseObject(prop.items, prefix, propType, typeRefs, primitiveTypes, classes);
                    cls.withProp(new ApexClassProperty(propType + '[]',propName));
                }
            }

            console.log(cls);
        }
    }

    classes.push(cls);
    typeRefs.push(objName);
}

var primitiveTypes = ['string', 'number', 'integer', 'boolean'];
var typeRefs = [];
var classes = [];
parseObject(data, 'CS_', 'Payload', typeRefs, primitiveTypes, classes);

let metadataFileContent = '<?xml version="1.0" encoding="UTF-8"?>\n<ApexClass xmlns="http://soap.sforce.com/2006/04/metadata">\n\t<apiVersion>49.0</apiVersion>\n\t<status>Active</status>\n</ApexClass>';

classes.forEach(cls => {
    let filename = `${cls.name}.cls`;
    fs.writeFileSync(`./${filename}`, cls.generate(), { flag: 'a'});
    fs.writeFileSync(`./${filename}.cls-meta.xml`,metadataFileContent, {flag: 'a'});
});