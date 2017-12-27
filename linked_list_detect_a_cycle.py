"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


# Implementation that takes O(n) additional memory, storing a reference to visited nodes in a set.
def has_cycle3(head):
    current = head
    traversed = set()
    while current is not None:
        if current in traversed or current.next is current:
            return True;
        traversed.add(current)
        current = current.next
    return False

# Implementation that takes O(1) additional memory, with Floyd algorithm.
def has_cycle2(head):
    if head is None:
        return False
    tortoise = head.next
    hare = None if tortoise is None else tortoise.next
    while tortoise is not None and hare is not None:
        if tortoise is hare:
            return True
        tortoise = tortoise.next
        hare = None if hare.next is None else hare.next.next
    return False

# Niftier implementation of Floyd algorithm
def has_cycle(head):
    tortoise = head
    hare = head
    while hare is not None and hare.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise is hare:
            return True
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