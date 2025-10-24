import os
import argparse
import maya.standalone
maya.standalone.initialize()
import maya.cmds

parser = argparse.ArgumentParser(description="Spawn a cube, sphere, and torus next to each other.")
parser.add_argument('-c', '--cube', help="Scale of the cube")
parser.add_argument('-s', '--sphere', help="Scale of the sphere")
parser.add_argument('-t', '--torus', help="Scale of the torus")
args = parser.parse_args()

print("Creating cube, sphere, and torus")

if not args.cube.scale:
    cube_scale = float(input("Enter scale for cube: "))
else:
    cube_scale = args.cube
if not args.sphere.scale:
    sphere_scale = float(input("Enter scale for sphere: "))
else:
    sphere_scale = args.sphere
if not args.torus.scale:
    torus_scale = float(input("Enter scale for torus: "))
else:
    torus_scale = args.torus

#These actually create the objects.
cube = maya.cmds.polyCube(name="myCube")[0]
maya.cmds.scale(cube_scale, cube_scale, cube_scale, cube)
maya.cmds.move(-5, 0, 0, cube)

sphere = maya.cmds.polySphere(name="mySphere")[0]
maya.cmds.scale(sphere_scale, sphere_scale, sphere_scale, sphere)
maya.cmds.move(0, 0, 0, sphere)

torus = maya.cmds.polyTorus(name="myTorus")[0]
maya.cmds.scale(torus_scale, torus_scale, torus_scale, torus)
maya.cmds.move(5, 0, 0, torus)

# this saves the file to wherever the script is being run from
output_path = os.path.join(os.getcwd(), "three_objects_scene.mb")
maya.cmds.file(rename=output_path)
maya.cmds.file(save=True)

print(f"Created cube, sphere, and torus with scales ({cube_scale}, {sphere_scale}, {torus_scale}).")
print(f"Scene saved as: {output_path}")