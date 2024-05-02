#!/usr/bin/python3
"""
A can unlock all module
"""


def canUnlockAll(boxes):
    """
    A method that determine if all the boxes can be opened

    Attr:
        boxes -  a list of lists
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()  # Keep track of the boxes visited
    queue = [0]  # Keep track of the boxes yet visited

    while queue:
        current_box = queue.pop(0)  # Pop a box from the queue
        if current_box not in visited:
            visited.add(current_box)
            keys = boxes[current_box]
            for key in keys:
                if 0 <= key < n:
                    queue.append(key)

    return len(visited) == n
