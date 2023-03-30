#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Lockboxes solution"""
    if (len(boxes) == 0 or type(boxes) != list):
        return false
    
    bl = len(boxes)
    keys = [0]
    # for i in range(len(keys)):
    for key in keys :
        for box in boxes[key]:
            if (box != 0 and box < bl):
                keys.append(box)

            # keys.update(boxes[key])

    # keys.add(0)
    # keys.append(0)
    keys = set(keys)

    if (len(keys) == len(boxes)):
        return True
    else:
        return False
