**Maya UI Tool — Image Plane Loader**



This tool lets users spawn pre-defined image planes directly into the Maya viewport. Each button in the UI loads a different image plane and attaches it to the perspective camera.



**Installation:**



Copy the entire folder to your Maya scripts directory:



Documents/maya/2025/scripts/



Open Maya.



In the Maya Script Editor, run the following:



import getFilePaths

getFilePaths.get\_image\_paths()





The custom window should appear with two buttons to spawn images.



**Usage**



Click either button to create an image plane in the scene. Each image plane will automatically attach to the current perspective camera. You can freely move, scale, or delete these planes afterward like any other geometry. It took a lot of tweaking to get this to work, please let me know if it works on your end so I can fix it if not. I admit I used some AI to walk me through the process of creating the maya window since there was no class recording but I did the code on my own.





