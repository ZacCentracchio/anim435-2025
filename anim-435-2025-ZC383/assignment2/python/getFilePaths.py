import os

def get_image_paths():
    global image_path_1, image_path_2
    base_path = os.path.dirname(os.path.abspath(__file__))
    return base_path

get_image_paths()
#this sets the image path directory for the images