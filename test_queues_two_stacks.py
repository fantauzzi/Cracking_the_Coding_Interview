from queues_two_stacks import MyQueue
import random
import pytest


def test_basic():
    queue = MyQueue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.peek() == 2
    assert queue.pop() == 2
    queue.put(4)
    assert queue.peek() == 3
    assert queue.pop() == 3
    assert queue.peek() == 4
    assert queue.pop() == 4

def test_pop_from_empty():
    queue = MyQueue()
    with pytest.raises(IndexError):
        queue.pop()

def test_big():
    queue = MyQueue()
    for i in range(int(10e6)):
        queue.put(i)
    for i in range(int(10e6)):
        assert queue.pop() == i





