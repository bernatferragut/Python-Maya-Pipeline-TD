import maya.cmds as cmds
# Gear Creation
def createGear( teeth=10, length=0.3 ): 
    """
    This function will create a gear with the given params
    Args: 
        teeth: number of teeth
        length: the length
    Returns:  
        A tuple with the transform, constructor and extrude node
    """
    # teeth are every alternate face, spans = teeth * 2
    spans = teeth * 2 
    transform, constructor = cmds.polyPipe(sa = spans)
    # selection of the faces
    sideFaces = range(spans*2, spans*3, 2) # between 40 and 60 and every second number
    # clear selection
    cmds.select( clear = True)
    # faceSelection
    for face in sideFaces:
        cmds.select('%s.f[%s]' % (transform, face), add=True)
    # extrude faces
    extrude = cmds.polyExtrudeFacet(localTranslateZ = length)[0]
    #unselect
    cmds.select( cl = True)
    # we print
    print("the final polyelement is: " + extrude)
    # we return for futur use
    return transform, constructor, extrude

#Gear Changes
def changeTeeth (constructor, extrude, teeth=10, length=1):
    # we get the number of spans
    spans = teeth*2
    #We edit the polyPipe node to change its teeth
    cmds.polyPipe(constructor, edit=True, sa=spans)
    # input components attr allow us to change the extrude node
    sideFaces = range(spans*2, spans*3, 2)
    faceNames = []
    for face in sideFaces:
        faceName = 'f[%s]' % (face)
        faceNames.append(faceName)
    # We define what we want to change where and how many tgrough the setAttr functions
    cmds.setAttr('%s.inputComponents' % (extrude), len(faceNames), *(faceNames), type= 'componentList') # expands faceName list
    #We edit the polyExtrude node to change its legth
    cmds.polyExtrudeFacet(extrude, edit=True, ltz = length)









                                                                                                 
