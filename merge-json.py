#!/usr/bin/env python

from genson import SchemaBuilder
import json
import os
import sys

files = sys.argv[1:]

builder = SchemaBuilder()
for f in files:
    with open(f) as curFile:
        builder.add_object(json.loads(curFile.read()))

with open('./master.json', 'w+') as f:
    f.write(str(builder.to_json()))
