#!/usr/bin/env node
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');
const argv = yargs(hideBin(process.argv))
    .command(
        'get-schema',
        'Generate JSON Schema file for given JSON data files',
        yargs => {
            yargs.option('f', {
                alias: 'files',
                type: 'array',
                demand: true,
                requiresArg: true,
                describe: 'One or more JSON data files',
                help: 'One or more JSON data files'
            })
        }
    )
    .command(
        'generate-apex',
        'Generates Apex classes for given JSON schema file',
        yargs => {
            yargs.option('s', {
                alias: 'schemafile',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Path of the JSON Schema file',
                help: 'Path of the JSON Schema file'
            })
        }
    )
    .demandCommand(1,1)
    .strict()
    .argv;

switch (argv._[0]) {
    case 'get-schema':
        const getSchema = require('./get-schema');
        getSchema(argv.f);
}

