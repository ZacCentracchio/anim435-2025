import maya.cmds as cmds
import getFilePaths
#imports the getFilePaths script to get the image paths
base_folder = getFilePaths.get_image_paths()
# importing the other script I mad efor this assignment
global image_path_1, image_path_2

image_path_1 = base_folder + "/Images/image1.jpg"
image_path_2 = base_folder + "/Images/image2.jpg"

def spawn_image_1():
    # Create a image plane and attaches to current camera
    image_plane = cmds.imagePlane(fileName=image_path_1,camera="persp")

def spawn_image_2():
    # Create a image plane and attaches to current camera
    image_plane = cmds.imagePlane(fileName=image_path_2,camera="persp")

my_window = cmds.window(title="My Window")
#This sets the columns to flex with the window size and this is also the title
my_col_layout_1 = cmds.columnLayout(adjustableColumn=True)
my_text_label = cmds.text(parent=my_col_layout_1, label="Press One Please")
#Button 1
my_col_layout_2 = cmds.columnLayout(adjustableColumn=True)
my_button = cmds.button(parent=my_col_layout_2, label="You Should Press This One", command = lambda x: spawn_image_1())
#Button 2
my_col_layout_3 = cmds.columnLayout(adjustableColumn=True)
my_button = cmds.button(parent=my_col_layout_3, label="Please Press The Other One", command = lambda x: spawn_image_2())
cmds.showWindow(my_window)
