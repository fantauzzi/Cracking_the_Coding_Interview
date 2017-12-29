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


def checkBST2(root):
    _, _, is_BST = get_min_max(root)
    return is_BST


# A more compact solution
def check_min_max(node, the_min, the_max):
    if node.data <= the_min or node.data >= the_max:
        return False
    if node.left and not check_min_max(node.left, the_min, min(the_max, node.data)):
        return False
    if node.right and not check_min_max(node.right, max(the_min, node.data), the_max):
        return False
    return True


def checkBST(root):
    is_BST = check_min_max(root, float('-inf'), float('inf'))
    return is_BST
