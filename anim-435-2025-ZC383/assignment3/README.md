**Maya UI Tool — Spawn three objects next to each other**

This tool lets the user spawn three objects next to each other and lets them adjust the scale of each. It spawns a cube, sphere, and torus side by side.

1. Initializes Maya in standalone mode.
2. Uses `argparse` to accept scale values for each object.
3. Creates a cube, sphere, and torus positioned next to each other.
4. Saves the resulting scene as `three_objects_scene.mb` in the current working directory.

Usage

Run the script using the `mayapy` alias in Git Bash or Terminal:

mayapy assignment3.py --cube 2.0 --sphere 1.5 --torus 3.0
or
mayapy assignment3.py -c 2.0 -s 1.5 -t 3.0

Post mortum:
I did not test this yet because of some errors with mayapy in gitbash. I really hope this works. I followed the example and changed my task from the image spawner becasue I thought tha would be too complicated to finish without testing. I  



