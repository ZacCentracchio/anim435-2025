import os

asset_name= os.environ.get('MY_ENV_VAR')

if not asset_name:
    print("global variable does not exist or was not set")
else:
    sphere = cmds.polySphere(name='asset_name' + "_geo")[0]

    print("created Sphere with the name " + 'asset_name')
