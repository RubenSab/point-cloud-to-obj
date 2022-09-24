#!/usr/bin/env python

import sys
source_file_name = sys.argv[1]

import os
new_file_name = os.path.splitext(source_file_name)[0]

def converter(destination_file_name):

    # load coordinates from source file
    with open(str(source_file), 'r') as f:
        lines = f.readlines()

    # remove useless additional values from vertex coordinates and format lines
    lines = [ f'v {" ".join(line.split(" ")[:3])}\n' for line in lines]

    # write vertex strings into the new Wavefront file
    with open(destination_file, 'w') as f:
        f.write('# https://github.com/RubenSab/point-cloud-to-obj/') # add watermark
        f.write('o ' + new_file_name) # add object name
        f.write(''.join(lines)) # write vertex coordinates
