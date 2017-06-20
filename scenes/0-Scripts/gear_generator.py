import maya.cmds as cmds

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
    # we print
    print("the final polyelement is: " + extrude)
    # we return for futur use
    return transform, constructor, extrude

                                                                                                 
