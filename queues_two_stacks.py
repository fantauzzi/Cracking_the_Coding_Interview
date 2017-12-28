from collections import deque

class MyQueue(object):
    def __init__(self):
        self.stack_1 = deque()
        self.stack_2 = deque()

    def pour_as_needed(self):
        if len(self.stack_2) == 0:
            if len(self.stack_1) == 0:
                raise IndexError
            self.stack_2.extendleft(self.stack_1)
            self.stack_1.clear()

    def peek(self):
        self.pour_as_needed()
        return self.stack_2[-1]

    def pop(self):
        self.pour_as_needed()
        return self.stack_2.pop()

    def put(self, value):
        self.stack_1.append(value)


if __name__ == '__main__':
    queue = MyQueue()
    t = int(input())
    for line in range(t):
        values = map(int, input().split())
        values = list(values)
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())

