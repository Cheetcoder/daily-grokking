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
from heapq import *  
  
  
class MedianOfAStream:  
  
  maxHeap = []  # containing first half of numbers  
  minHeap = []  # containing second half of numbers  
  
  def insert_num(self, num):  
    if not self.maxHeap or -self.maxHeap[0] >= num:  
      heappush(self.maxHeap, -num)  
    else:  
      heappush(self.minHeap, num)  
  
    # either both the heaps will have equal number of elements or max-heap will have one  
    # more element than the min-heap    if len(self.maxHeap) > len(self.minHeap) + 1:  
      heappush(self.minHeap, -heappop(self.maxHeap))  
    elif len(self.maxHeap) < len(self.minHeap):  
      heappush(self.maxHeap, -heappop(self.minHeap))  
  
  def find_median(self):  
    if len(self.maxHeap) == len(self.minHeap):  
      # we have even number of elements, take the average of middle two elements  
      return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0  
  
    # because max-heap will have one more element than the min-heap  
    return -self.maxHeap[0] / 1.0  
```
## 3. Meeting Rooms II

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return _the minimum number of conference rooms required_.

**Example 1:**

**Input:** intervals = [[0,30],[5,10],[15,20]]
**Output:** 2

**Example 2:**

**Input:** intervals = [[7,10],[2,4]]
**Output:** 1

```python
def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))
        
        time.sort(key=lambda x: (x[0], x[1]))
        
        count = 0
        max_count = 0
        for t in time:
            count += t[1]
            max_count = max(max_count, count)
        return max_count

```
