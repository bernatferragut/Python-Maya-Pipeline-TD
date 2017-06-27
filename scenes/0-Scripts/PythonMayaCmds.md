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

# getAttr

import maya.cmds as cmds
cmds.polyCube(n="cube")
cmds.gettAttr("cube.tx")
cmds.gettAttr("cube.scaleY")
cmds.gettAttr( "cube.visibility", True)
cmds.gettAttr("cube.rotate") > Tuple
cmds.gettAttr("cube.translateX")

# setAttr
import maya.cmds as cmds
cmds.polyCube(n="cube")
cmds.setAttr("cube.scaleX", 2)
cmds.setAttr("cube.scaleY", 2)
cmds.setAttr( "cube.visibility", True)
cmds.setAttr("cube.rotate", 0, 0, 0, type="double3")
cmds.setAttr("cube.translateX", keyable=True)

# string

s1 = 'String 1'
s2 = 'Sring 2'

summ = s1 + 'and' + s2

number_of_chars = len(s1)

s[0]        # First character
s[-1]       # Last character
s.upper()   # To Uppercase
s.lower()   # To Lower
s.split()   # Split letters string
s.split(' ')# Split by space

" new line: \n"
" new tab: \t"
" backslash: \\"
" single quotes: \""




