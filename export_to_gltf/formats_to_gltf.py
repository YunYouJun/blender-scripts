# Example:
# blender -b empty.blend --python ./export_to_gltf/formats_to_gltf.py -- ./test/obj/airship.obj

import bpy
import sys
import os.path

__version__ = 0.1

def clean_all_object():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

def get_filepath():
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--":
            break
    src_filepath = sys.argv[i+1] ? sys.argv[i+1]
    return src_filepath

def convert_to_glb(format, filepath):
    convert_func = {
        # Wm Operators
        # https://docs.blender.org/api/current/bpy.ops.wm.html
        '.abc': bpy.ops.wm.alembic_import,
        '.dae': bpy.ops.wm.collada_import,
        # Import Scene Operators
        # https://docs.blender.org/api/current/bpy.ops.import_scene.html
        '.fbx': bpy.ops.import_scene.fbx,
        '.gltf': bpy.ops.import_scene.gltf,
        '.obj': bpy.ops.import_scene.obj,
        '.x3d': bpy.ops.import_scene.x3d,
        # Import Mesh Operators
        # https://docs.blender.org/api/current/bpy.ops.import_mesh.html
        '.ply': bpy.ops.import_mesh.ply,
        '.stl': bpy.ops.import_mesh.stl,
    }
    convert_func[format](filepath = filepath)

def main():
    # get filepath & ext
    src_filepath = get_filepath()
    (src_root, src_ext) = os.path.splitext(src_filepath)

    # start with an empty scene
    clean_all_object()

    # convert
    convert_to_glb(src_ext, src_filepath)

    # default to src folder
    bpy.ops.export_scene.gltf(filepath = src_root)

if __name__ == '__main__':
    main()
