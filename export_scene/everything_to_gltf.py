# import bpy
import sys
import os.path
import time

__version__ = 0.1
exported_folder = './exported'

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def cost_time(func):
    def inner(*args,**kw):
        start_time = time.time()
        func(*args,**kw)
        end_time = time.time()
        print(color.GREEN + 'Cost time: ', end_time - start_time, 's' + color.END)
    return inner

def get_filename():
    src_filepath = sys.argv[2]
    basename = os.path.basename(src_filepath)
    return os.path.splitext(basename)[0]

@cost_time
def main():
    filename = get_filename()
    # default to exported folder
    print(bpy.app.build_time)
    bpy.ops.export_scene.gltf(filepath = exported_folder + filename)


if __name__ == '__main__':
    main()

# # Read a .3ds file
# bpy.ops.import_scene.autodesk_3ds(filepath=file)

# # Write a .obj file
# outfile = os.path.splitext(file)[0]+".obj"
# bpy.ops.export_scene.obj(filepath=outfile)
