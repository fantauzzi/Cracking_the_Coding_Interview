from trees_is_this_a_BST import checkBST

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def test_1_node():
    r = node(10)
    assert checkBST(r)


def test_basic_yes():
    r = node(10)
    r.left = node(0)
    r.right = node(20)
    assert checkBST(r)


def test_basic_no():
    r = node(10)
    r.left = node(0)
    r.right = node(5)
    assert not checkBST(r)


def test_failed_TC():
    n0 = node(3)
    n1 = node(2)
    n2 = node(6)
    n3 = node(1)
    n4 = node(4)
    n5 = node(5)
    n6 = node(7)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    assert not checkBST(n0)
