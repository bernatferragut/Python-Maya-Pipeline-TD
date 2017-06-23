# Python Maya Commands ( cmds )


javascript
import maya.cmds as cmds

# Create polygon sphere > creates a list of nodes

cmds.polySphere()

# Create polygon sphere with a radius of 10

cmds.polySphere(r = 10)

# The help command

cmds.help('polySphere')

# Command Modes:  Create, Query and Edit

cmds.polySphere(query = True, r = True) 

cmds.polySphere(edit = True, r = 21)

# SUPER: ls > display all objects in the scene filtered by flags

import maya.cmds as cmds

cmds.ls()
cmds.ls(selection = True)
cmds.ls(cameras = True, shapes =  True)

# SUPER: select > used to control the selected objects in a scene

import maya.cmds as cmds

cmds.select( clear = True)
cmds.select( 'polyCylinder', add = True, )
cmds.select('polyCube', replace = True)






