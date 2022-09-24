#!/usr/bin/env python

import sys
source_file = sys.argv[1]

# automatically choose the new file's name if the user hasn't chosen one
if len(sys.argv) == 2:
    destination_file = sys.argv[1]+".obj"
else:
    destination_file = sys.argv[2]



def converter(source_file, destination_file):

    # load lines from source file
    with open(str(source_file), "r") as f:
        lines = f.readlines()

    # get vertex coordinates from lines
    vertices = [ list(map(float, line.rstrip().split())) for line in lines ]

    # format vertices into .obj vertex strings, for more info visit https://en.wikipedia.org/wiki/Wavefront_.obj_file#Geometric_vertex
    lines_to_write = [ "v "+"".join( [str(coord)+" " for coord in vertex] ).rstrip()+"\n" for vertex in vertices ]

    # write vertex strings into the new Wavefront file
    with open(destination_file, "w") as f:
        f.write("".join(lines_to_write))
