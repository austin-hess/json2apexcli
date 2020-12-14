const { spawn } = require('child_process');

const getSchema = (targetDir, pattern, outputPath) => {

    const pyProg = spawn('python', ['./get-schema.py', '-d', targetDir, '-p', pattern, '-o', outputPath]);

    pyProg.stdout.on('data', data => {
        console.log(data.toString());
    });
}

module.exports = getSchema;