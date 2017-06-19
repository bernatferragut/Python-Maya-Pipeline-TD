# Cube Handler Maya Program

import maya.cmds as cmds

cube = cmds.polyCube()
cubeShape = cube[0]

circle = cmds.circle()
circleShape = circle[0]

cmds.parent(cubeShape, circleShape)

cmds.setAttr("pCube1.translate", lock = True )
cmds.setAttr("pCube1.rotate", lock = True )
cmds.setAttr("pCube1.scale", lock = True )
