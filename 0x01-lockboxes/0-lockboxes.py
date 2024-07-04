#!/usr/bin/python3
'''LockBoxes Challenge'''
from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set()
    to_visit = [0]  # Start with box 0 (the first box)

    while to_visit:
        current_box = to_visit.pop(0)
        visited.add(current_box)
        for key in boxes[current_box]:
            if key < n and key not in visited:
                to_visit.append(key)

    return len(visited) == n
