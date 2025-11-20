import os
import logging
import json
import datetime


import maya.cmds as cmds
#import maya.standalone
#maya.standalone.initialize()



# Reads the asset name, task name, and user name from environment variables
asset_env = os.environ.get('ASSET')
task = os.environ.get('TASK')
user = os.environ.get('USER')
if user is None:
    logger.warning("USER environment variable not set")

f = open('metadata.json', 'w')

scene_metadata = {
    "scene_name": task + ".mb",
    "username": user,
    "export_Time": datetime.datetime.now().isoformat(),
    "version": cmds.about(version=True),
}

json.dump(scene_metadata, f)
print(scene_metadata)
logger = logging.getLogger(__name__)
FORMAT = "[%(asctime)s][%(filename)s][%(levelname)s] %(msg)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

def main_ui():
    
    
    
    # Default values
    cube_scale = 1.0
    sphere_scale = 1.0
    torus_scale = 1.0
    asset_choice = asset_env if asset_env else "all"

    # Create window
    if cmds.window("mainWin", exists=True):
        cmds.deleteUI("mainWin")
    win = cmds.window("mainWin", title="Create & Export Objects")
    cmds.columnLayout(adjustableColumn=True)

    #this edits the scale in a float field.
    cube_scale_field = cmds.floatFieldGrp(label="Cube Scale", value1=cube_scale)
    sphere_scale_field = cmds.floatFieldGrp(label="Sphere Scale", value1=sphere_scale)
    torus_scale_field = cmds.floatFieldGrp(label="Torus Scale", value1=torus_scale)
    print(cube_scale, sphere_scale, torus_scale)
    #This creates the drop down and populates with each option
    asset_menu = cmds.optionMenuGrp(label="Asset to Export")
    cmds.menuItem(label="cube")
    cmds.menuItem(label="sphere")
    cmds.menuItem(label="torus")
    cmds.menuItem(label="all")

    #This handles all of the object creation and exporting
    def create_and_export(*args):


        if cube_scale <= 0 or sphere_scale <= 0 or torus_scale <= 0:
            logger.error("All scales must be a positive number")
            return none
        

        c_scale = cmds.floatFieldGrp(cube_scale_field, q=True, value1=True)
        s_scale = cmds.floatFieldGrp(sphere_scale_field, q=True, value1=True)
        t_scale = cmds.floatFieldGrp(torus_scale_field, q=True, value1=True)
        asset = cmds.optionMenuGrp(asset_menu, q=True, value=True)

        cube = cmds.polyCube(name="myCube")[0]
        cmds.scale(c_scale, c_scale, c_scale, cube)
        cmds.move(-5, 0, 0, cube)

        sphere = cmds.polySphere(name="mySphere")[0]
        cmds.scale(s_scale, s_scale, s_scale, sphere)
        cmds.move(0, 0, 0, sphere)

        torus = cmds.polyTorus(name="myTorus")[0]
        cmds.scale(t_scale, t_scale, t_scale, torus)
        cmds.move(5, 0, 0, torus)

        output_path = os.path.join(os.getcwd(), "three_objects_scene.mb")
        cmds.file(rename=output_path)
        cmds.file(save=True)

        if not cmds.pluginInfo("fbxmaya", q=True, loaded=True):
            cmds.loadPlugin("fbxmaya")

        #   Formats this information into a structured filepath (that you can define)
        def export_specific_object(object_name,  file_name):
            cmds.select(object_name)
            export_path = os.path.join(os.getcwd(), "exports", f"{file_name}.fbx")
            #Exports the asset as an FBX
            cmds.file(export_path, force=True, options="v=0;", type="FBX export", exportSelected=True)

            
            logger.info(f"Exported {object_name} to {export_path}")

        if asset == "cube":
            export_specific_object(cube,  asset)
        elif asset == "sphere":
            export_specific_object(sphere,  asset)
        elif asset == "torus":
            export_specific_object(torus,  asset)
        elif asset == "all":
            cmds.select([cube, sphere, torus])
            export_path = os.path.join(os.getcwd(), "all_objects.fbx")
            cmds.file(export_path, force=True, options="v=0;", type="FBX export", exportSelected=True)
        else:
            print("Invalid asset selection.")

    cmds.button(label="Create & Export", command=create_and_export)
    cmds.showWindow(win)
    

main_ui()