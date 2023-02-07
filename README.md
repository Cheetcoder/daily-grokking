# Daily Grokking Prep

## 1. Task Scheduler 
- [Task Scheduler Prompt](./problems/task_scheduler.md)
- [Python - Try it yourself](./practice/task_scheduler.py)

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

Hints: 
- You can use a Heap/Priority queue

```python
from collections import Counter
import heapq

def leastInterval(tasks, n):
    task_counts = Counter(tasks)
    task_heap = [-count for count in task_counts.values()]
    heapq.heapify(task_heap)

    units_of_time = 0
    while task_heap:
        i, temp = 0, []
        for i in range(n+1):
            if task_heap:
                temp.append(-heapq.heappop(task_heap))
                units_of_time += 1
            else:
                break
        for count in temp:
            if count + 1 < 0:
                heapq.heappush(task_heap, count+1)

        if not task_heap and i <= n:
            break

    return units_of_time

```

## 2. Find median from Data stream

- [Find Median from Data Stream Prompt](./problems/Find_Median_From_Data_Stream.md)
- [Python - Try it yourself](./practice/find_median_data_stream.py)


Design a class to calculate the median of a number stream. The class should have the following two methods:

1.  `insertNum(int num)`: stores the number in the class
2.  `findMedian()`: returns the median of all numbers inserted in the class

Hints: 
- You can use a Heap/Priority queue (two of them)


```python
import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize two heaps, one max heap to store the smaller half of the numbers and one min heap to store the larger half.
        """
        self.small = []  # max heap to store the smaller half of the numbers
        self.large = []  # min heap to store the larger half of the numbers

    def insertNum(self, num):
        """
        Insert the given number into the correct heap, maintaining the balance between the two heaps.
        """
        if len(self.small) == 0 or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # Rebalance the two heaps if they become unbalanced
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        Return the median of the numbers inserted into the class.
        """
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
```
_____________________

### Resources

- https://neetcode.io/practice - Many of the problems above can be found here, with video and code solultions
- https://replit.com/ - Real time collaboration to pair program
- https://obsidian.md/ - A markdown to take notes and help you practice without code formatting 
