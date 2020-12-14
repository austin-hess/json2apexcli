#!/usr/bin/env node
const yargs = require('yargs/yargs');
const { hideBin } = require('yargs/helpers');
const argv = yargs(hideBin(process.argv))
    .command(
        'get-schema',
        'Generate JSON Schema file for given JSON data files',
        yargs => {
            yargs.option('d', {
                alias: 'targetdir',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Directory in which to search for the given pattern in filenames',
                help: 'Directory in which to search for the given pattern in filenames'
            }),
            yargs.option('p', {
                alias: 'pattern',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Python-style regex surrounded in quotes to match on filenames',
                help: 'Python-style regex surrounded in quotes to match on filenames'
            }),
            yargs.option('o', {
                alias: 'outputpath',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Path for output file',
                help: 'Path for output file'
            })
        }
    )
    .command(
        'generate-apex',
        'Generates Apex classes for given JSON schema file',
        yargs => {
            yargs.example(
                './json.apex.js generate-apex -s master.json -p CS_ -c Payload'
            )
            yargs.option('s', {
                alias: 'schemafile',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Path of the JSON Schema file',
                help: 'Path of the JSON Schema file'
            })
            yargs.option('p', {
                alias: 'prefix',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Prefix for the resulting class',
                help: 'Prefix for the resulting class'
            })
            yargs.option('c', {
                alias: 'className',
                type: 'string',
                demand: true,
                requiresArg: true,
                describe: 'Name of the resulting class',
                help: 'Name of the resulting class'
            })
        }
    )
    .demandCommand(1,1)
    .strict()
    .argv;

switch (argv._[0]) {
    case 'get-schema':
        const getSchema = require('./get-schema.js');
        getSchema(argv.d, argv.p, argv.o);
        break;
    case 'generate-apex':
        const genApex = require('./generate-apex.js');
        genApex(argv.s, argv.p, argv.c);
        break;
}

