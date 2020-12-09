class ApexClass {
    props = []

    constructor(name) {
        this.name = name;
    }

    withProp(prop) {
        this.props.push(prop);
    }
    
    generate() {
        let classData = `public without sharing class ${this.name} {\n`;
        
        this.props.forEach(prop => {
            classData += `\tpublic ${prop.typeRef} ${prop.name};\n`;
        });

        classData += '}';

        return classData;
    }
}

class ApexClassProperty {
    constructor(typeRef, name) {
        this.typeRef = typeRef;
        this.name = name;
    }
}

module.exports = {
    ApexClass,
    ApexClassProperty
};