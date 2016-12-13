import bpy
from random import randint
bpy.ops.mesh.primitive_cube_add()

# https://www.blender.org/api/blender_python_api_2_78a_release/contents.html
# https://www.blender.org/manual/editors/python_console.html


#how many cubes you want to add
count = 10

for c in range(0,count):
    x = randint(-10,10)
    y = randint(-10,10)
    z = randint(-10,10)
    bpy.ops.mesh.primitive_cube_add(location=(x,y,z))
