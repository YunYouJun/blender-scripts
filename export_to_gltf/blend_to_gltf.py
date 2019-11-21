# Example:
# blender -b ./imported/airship.blend --python ./export_to_gltf/blend_to_gltf.py

import bpy
import sys
import os.path

__version__ = 0.1

def main():
    filename = get_filename()
    bpy.ops.export_scene.gltf(filepath='./exported/' + filename)
    # default to cur folder

def get_filename():
    src_filepath = sys.argv[2]
    basename = os.path.basename(src_filepath)
    return os.path.splitext(basename)[0]

if __name__ == '__main__':
    main()
