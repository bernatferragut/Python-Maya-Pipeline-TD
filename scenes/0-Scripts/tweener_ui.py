# Maya UI project

from maya import cmds

def tween(percentaje, obj=None, attrs=None, selection=True):
    # if obj is not given adn selection = False, error early
    if not obj and not selection:
        raise valueError("No object given to tween")
    # if no obj is especified, get it from first selection
    if not obj:
        obj = cmds.sl(selection=True)[0]

    if not attrs:
        attrs = cmds.listAttr(obj, keyable = True)

    print obj, attr