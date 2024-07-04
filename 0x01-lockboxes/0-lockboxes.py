#!/usr/bin/python3
'''LockBoxes Challenge'''

from collections import deque


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened or not.

    Args:
        boxes (list of lists): Each sublist contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''
    n = len(boxes)
    visited = set()
    to_visit = deque([0])  # Start with box 0 (the first box)

    while to_visit:
        current_box = to_visit.popleft()
        visited.add(current_box)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                to_visit.append(key)

    return len(visited) == n
