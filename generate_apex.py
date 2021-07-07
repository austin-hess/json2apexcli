#!/usr/bin/env python

import json
import click
from apex_generator import Json2ApexGenerator

@click.command(
    help="USAGE: ./generate-schema.py --schemapath ./schema.json --classname Main --prefix NS --outputdir ./output/"
)
@click.option(
    '--schemapath', 
    's', 
    multiple=False,
    default=None, 
    help="Use --schemapath to specify the schema file to use")
@click.option(
    '--classname', 
    'c', 
    multiple=False,
    default=None, 
    help="Use --classname to specify the name of the parent class")
@click.option(
    '--prefix', 
    'p', 
    multiple=False, 
    default=None, 
    help="Use --prefix if you want to specify a class prefix")
@click.option(
    '--outputdir',
    'o',
    multiple=False,
    default='master.json',
    help="Use --outputdir to specify which directory you want the Apex classes to be dropped in"
)
def main(s, c, p, o):
    print(s, c, p, o)
    with open(s, 'r') as f:
        json_schema = json.loads(f.read())
        generator = Json2ApexGenerator(json_schema)
        generator.set_output_path(o)
        generator.set_prefix(p)
        generator.generate(c)

if __name__ == '__main__':
    main()