const { spawn } = require('child_process');

const getSchema = (dataFiles, outputPath) => {

    const pyProg = spawn('python', ['./get-schema.py', '--files', ...dataFiles, '--outputpath', outputPath]);

    pyProg.stdout.on('data', data => {
        console.log(data.toString());
    });
}

module.exports = getSchema;