# blender-scripts

Blender Python Scripts

## Ref

- [Blender Python API Documentation](https://docs.blender.org/api/current/)
- [blender_scipts | GitHub](https://github.com/ankurhanda/blender_scripts)

## Intro

Ok, let's run python by blender.

> At first, ensure that you had config blender environment.
> rf [Launching from the Command Line](https://docs.blender.org/manual/en/latest/advanced/command_line/launch/index.html)

```sh
blender -b file --python /home/me/my_script.py
```

## Function

### Convert to glb/gltf

- [x] blend
- [x] fbx
- [x] gltf
- [x] obj
- [x] x3d
- [x] ply
- [x] stl

| Format | Test |
| --- | --- |
| blend | √ |
| dae | √ |
| fbx | √ |
| obj | √ |
| ply | √ |
| stl | √ |

Blender to gltf:

```sh
blender -b <Your blend file> --python ./export_to_gltf/blend_to_gltf.py
# Example:
blender -b ./imported/airship.blend --python ./export_to_gltf/blend_to_gltf.py
```

Other formats to gltf:

```sh
blender -b empty.blend --python ./export_to_gltf/formats_to_gltf.py -- <Your File Path>
# Example
blender -b empty.blend --python ./export_to_gltf/formats_to_gltf.py -- ./test/obj/airship.obj
```

## Stucture

| File/Folder Name | Function |
| --- | --- |
| empty.blend | an empty blender file as a transfer station |
| export_to_gltf | python script folder for exporting to gltf|
| test | models for test |
| .pylintrc | to ignore bpy module ont exist error in python (beacuse we use python in blender) |

## Todo

- [ ] optional [gltf | glb]
