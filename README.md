# point cloud to obj
A Python script that converts point clouds to Wavefront (.obj) files


## installation
Launch ```git clone https://github.com/RubenSab/point-cloud-to-obj.git``` from terminal or download ZIP folder


## usage
Launch ```python3 cloud_to_obj [source file name]``` from terminal


## file extensions and specifications

### source file
Every extension is valid (even no extension).
Specifications:
```
[first vertex x coordinate] [first vertex y coordinate] [first vertex z coordinate]
[second vertex x coordinate] [second vertex y coordinate] [second vertex z coordinate]
...
[last vertex x coordinate] [last vertex y coordinate] [last vertex z coordinate]
```

### new Wavefront file created:
.obj extension
Specifications:
```
o [cloud name]
v [first vertex x coordinate] [first vertex y coordinate] [first vertex z coordinate]
v [second vertex x coordinate] [second vertex y coordinate] [second vertex z coordinate]
...
v [last vertex x coordinate] [last vertex y coordinate] [last vertex z coordinate]
```
