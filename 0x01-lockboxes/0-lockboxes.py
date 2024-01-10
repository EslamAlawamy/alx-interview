#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """
    Args: A list of lockboxes.
    Returns: A list of unlocked boxes.
    """
    box_count = len(boxes)
    visited = [False] * box_count
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < box_count and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
