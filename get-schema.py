#!/usr/bin/env python

from genson import SchemaBuilder
import click
import json
import os
import re

@click.command(
    help="USAGE: ./get-schema.py --targetdir ./ --pattern '.*\.json' --outputpath ./master.json"
)
@click.option(
    '--targetdir', 
    'd', 
    multiple=False,
    default=None, 
    help="Use --targetdir to include a target directory")
@click.option(
    '--pattern', 
    'p', 
    multiple=False, 
    default=None, 
    help="Use --pattern to include regex that looks for files in the given directory")
@click.option(
    '--outputpath',
    'o',
    multiple=False,
    default='master.json',
    help="Use --outputpath to specify the path of the output JSON file"
)
def main(d,p,o):

    dir = '{}'.format(d)

    print('\nLooking for files matching  "{}"  in directory  "{}"  to generate schema file  "{}"'.format(p, dir, o))

    matching_files = [f for f in os.listdir(dir) if re.match(p,f) is not None]

    print('\nGenerating schema with following files: ')
    for f in matching_files:
        print('{}\{}'.format(dir, f))

    builder = SchemaBuilder()

    for file in matching_files:
        with open('{}/{}'.format(dir, file)) as curFile:
            builder.add_object(json.loads(curFile.read()))

    with open(o, 'w+') as curFile:
        curFile.write(str(builder.to_json()))
    
    click.echo('\nCreated schema file {}.'.format(o))

if __name__ == '__main__':
    main()
