#!/bin/python3

import sys
import heapq

class Rolling_median_finder():
    def __init__(self):
        self.heap_left = []  # It will be used as max-heap by reversing the sign of numbers added to it
        self.heap_right = []  # A min-heap
        self.median = None  # Only used in roll2() to keep track of the latest computed median

    def roll2(self, item):
        # Initialize the median for step 0 of the algorithm
        if self.median is None:
            self.median = item
        # Add the new item to the correct heap
        if item >= self.median:
            heapq.heappush(self.heap_right, item)
        else:
            heapq.heappush(self.heap_left, -item)
        # Ensure that the difference in length between the two heaps is at most 1
        if len(self.heap_right) > len(self.heap_left) + 1:
            popped = heapq.heappop(self.heap_right)
            heapq.heappush(self.heap_left, -popped)
        elif len(self.heap_left) > len(self.heap_right) + 1:
            popped = heapq.heappop(self.heap_left)
            heapq.heappush(self.heap_right, -popped)
        # Compute and return the updated median
        if len(self.heap_left) == len(self.heap_right):
            self.median = (-self.heap_left[0] + self.heap_right[0]) / 2
        else:
            self.median = -self.heap_left[0] if len(self.heap_left) > len(self.heap_right) else self.heap_right[0]
        return self.median

    # A more compact solution, that doesn't need to keep track of the last median computed
    def roll(self, item):
        # Push new item to the left heap (max-heap)
        heapq.heappush(self.heap_left, -item)
        # If the total number of items between the two heaps is even...
        if (len(self.heap_left) + len(self.heap_right))  % 2 == 0:
            # ... then pop the head from the left heap and add it to the right heap
            popped = heapq.heappop(self.heap_left)
            heapq.heappush(self.heap_right, -popped)
        else:
            # If instead it is odd...
            if len(self.heap_right) > 0 and -self.heap_left[0] > self.heap_right[0]:
                # ...then pop the head from each heap, and add it to the other one
                left_head = heapq.heappop(self.heap_left)
                right_head = heapq.heappop(self.heap_right)
                heapq.heappush(self.heap_right, -left_head)
                heapq.heappush(self.heap_left, -right_head)

        # Determine and return the median
        if (len(self.heap_left) + len(self.heap_right)) % 2 == 0:
            # If the total number of items is even, the median is the average between the two heap heads
            return (self.heap_right[0] -self.heap_left[0]) / 2
        else:
            # Otherwise it is the head of the left heap
            return -self.heap_left[0]


if __name__ == '__main__':
    finder = Rolling_median_finder()
    n = int(input().strip())
    a = []
    a_i = 0
    for a_i in range(n):
        a_t = int(input().strip())
        median = finder.roll(a_t)
        print('{:.1f}'.format(median))
