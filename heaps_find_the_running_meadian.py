#!/bin/python3

import sys
import heapq

class Rolling_median_finder():
    def __init__(self):
        self.heap_left = []
        self.heap_right = []
        self.median = None

    def roll(self, item):
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


if __name__ == '__main__':
    finder = Rolling_median_finder()
    n = int(input().strip())
    a = []
    a_i = 0
    for a_i in range(n):
        a_t = int(input().strip())
        median = finder.roll(a_t)
        print('{:.1f}'.format(median))
