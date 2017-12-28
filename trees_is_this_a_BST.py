""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def get_min_max(root):
    the_min = root.data
    the_max = root.data
    if root.left is not None:
        left_min, left_max, is_BST = get_min_max(root.left)
        if not is_BST:
            return 0, 0, False
        if left_max >= root.data:
            return False, 0, 0
        if left_min < the_min:
            the_min = left_min
        if left_max > the_max:
            the_max = left_max
    if root.right is not None:
        right_min, right_max, is_BST = get_min_max(root.right)
        if not is_BST:
            return 0, 0, False
        if right_min <= root.data:
            return False, 0, 0
        if right_min < the_min:
            the_min = right_min
        if right_max > the_max:
            the_max = right_max
    return the_min, the_max, True


def checkBST(root):
    _, _, is_BST = get_min_max(root)
    return is_BST
