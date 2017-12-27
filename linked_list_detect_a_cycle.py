"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    current = head
    traversed = set()
    while current is not None:
        if current in traversed or current.next is current:
            return True;
        traversed.add(current)
        current = current.next
    return False


def test_no_cycle():
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

    n1 = Node('C')
    n2 = Node('B', n1)
    n3 = Node('A', n2)
    res = has_cycle(n3)
    assert not res


def test_cycle():
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

    n1 = Node('C')
    n2 = Node('B', n1)
    n3 = Node('A', n2)
    n1.next = n2
    res = has_cycle(n3)
    assert res


def test_cycle_on_itself():
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node

    n1 = Node('C')
    n2 = Node('B', n1)
    n3 = Node('A', n2)
    n1.next = n1
    res = has_cycle(n3)
    assert res


def test_empty_list():
    res = has_cycle(None)
    assert not res