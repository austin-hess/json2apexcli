const { spawn } = require('child_process');

const getSchema = (dataFiles) => {

    const pyProg = spawn('python', ['./merge-json.py', ...dataFiles]);

    pyProg.stdout.on('data', data => {
        console.log(data.toString());
    });
}

module.exports = getSchema;