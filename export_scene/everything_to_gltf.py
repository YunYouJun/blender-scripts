import bpy
import sys
import os.path

# Read a .3ds file
bpy.ops.import_scene.autodesk_3ds(filepath=file)

# Write a .obj file
outfile = os.path.splitext(file)[0]+".obj"
bpy.ops.export_scene.obj(filepath=outfile)