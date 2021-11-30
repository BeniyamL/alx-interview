#!/usr/bin/python3
""" a python method to check if the rooms/boxes can be opened with keys """

def canUnlockAll(boxes):
    """ A method to retur true if all boxes can be opend else false
    the first box is always empty and each box named from 0 to n-1
    after you open the box, you may get a key for other boxes 
    """
    open_box = {}
    ln = len(boxes)
    open_box[0] = 0
    idx = 0;
    for box in boxes:
        if box:
            for key in box:
                if idx in open_box:
                    if key and key < ln:
                        open_box[key] = key
                    if key < ln:
                        for val in boxes[key]:
                            if val:
                                open_box[val] = val
                else:
                    return (False)
        else:
           if idx not in open_box:
               return False;
        idx += 1
    return (True)
