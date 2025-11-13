Export an object as an fbx using gitbash

This tool takes environment variables and uses them to export specific objects to FBX. it takes the file structure from your environment variables.

**Usage**

in the gitbash window type 

export ASSET=cube
export TASK=exportCube
export USER=*your username here*

This will be used later for whchc object you want to export, and what the folder names will be called.

Then open maya using the same window.

in maya code editer, paste the code from midterm.py into the python window.
or you can open the file in the window.

A window will pop up with three objects and a number next to them. this number will determine the scale of each of them. 

Below this there is a button that says export. after pressing this, the object you chose in the environment will export to your current directory in a folder that you determined with your username and task. 

------------

There are now three lggoning tools that will let you know if you are interacting with the tool improperly. One is if you give a negetive scale on any of the objects. two is letting you know where you exported the file. Three is letting you know as a warning that the environment variable was never set correctly.


