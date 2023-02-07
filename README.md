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

Solution:

We can't really process the given meetings in any random order. The most basic way of processing the meetings is in increasing order of their `start times` and this is the order we will follow. After all, it makes sense to allocate a room to the meeting that is scheduled for 9 a.m. in the morning before you worry about the 5 p.m. meeting, right?

Let's do a dry run of an example problem with sample meeting times and see what our algorithm should be able to do efficiently.

We will consider the following meeting times for our example `(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)`. The first part of the tuple is the start time for the meeting and the second value represents the ending time. We are considering the meetings in a sorted order of their start times. The first diagram depicts the first three meetings where each of them requires a new room because of collisions.

![](https://leetcode.com/problems/meeting-rooms-ii/solutions/168762/Figures/253/253_Meeting_Rooms_II_Diag_1.png)

The next 3 meetings start to occupy some of the existing rooms. However, the last one requires a new room altogether and overall we have to use 4 different rooms to accommodate all the meetings.

![](https://leetcode.com/problems/meeting-rooms-ii/solutions/168762/Figures/253/253_Meeting_Rooms_II_Diag_2.png)

Sorting part is easy, but for every meeting how do we find out efficiently if a room is available or not? At any point in time we have multiple rooms that can be occupied and we don't really care which room is free as long as we find one when required for a new meeting.

A naive way to check if a room is available or not is to iterate on all the rooms and see if one is available when we have a new meeting at hand.

> However, we can do better than this by making use of Priority Queues or the Min-Heap data structure.

Instead of manually iterating on every room that's been allocated and checking if the room is available or not, we can keep all the rooms in a min heap where the key for the min heap would be the ending time of meeting.

So, every time we want to check if **any** room is free or not, simply check the topmost element of the min heap as that would be the room that would get free the earliest out of all the other rooms currently occupied.

If the room we extracted from the top of the min heap isn't free, then `no other room is`. So, we can save time here and simply allocate a new room.

Let us look at the algorithm before moving onto the implementation.

**Algorithm**

1.  Sort the given meetings by their `start time`.
2.  Initialize a new `min-heap` and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3.  For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4.  If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5.  If not, then we allocate a new room and add it to the heap.
6.  After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
```
