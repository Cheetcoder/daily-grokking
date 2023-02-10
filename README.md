# Daily Grokking Prep

## 1. Task Scheduler 
- [Task Scheduler Prompt](./problems/task_scheduler.md)
- [Python - Try it yourself](./practice/task_scheduler.py)

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

Hints: 
- You can use a Heap/Priority queue

Click details to see solution in python:

<details>

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
</details>

## 2. Find median from Data stream

- [Find Median from Data Stream Prompt](./problems/Find_Median_From_Data_Stream.md)
- [Python - Try it yourself](./practice/find_median_data_stream.py)


Design a class to calculate the median of a number stream. The class should have the following two methods:

1.  `insertNum(int num)`: stores the number in the class
2.  `findMedian()`: returns the median of all numbers inserted in the class

Hints: 
- You can use a Heap/Priority queue (two of them)

<details>

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

</details>

## 3. Meeting Rooms II

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return _the minimum number of conference rooms required_.

**Example 1:**

**Input:** intervals = [[0,30],[5,10],[15,20]]
**Output:** 2

**Example 2:**

**Input:** intervals = [[7,10],[2,4]]
**Output:** 1

#### Approach 1

**Algorithm**

1.  Sort the given meetings by their `start time`.
2.  Initialize a new `min-heap` and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3.  For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4.  If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5.  If not, then we allocate a new room and add it to the heap.
6.  After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

<details>

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

</details>


#### Approach 2: Chronological Ordering

**Algorithm**


1.  Separate out the start times and the end times in their separate arrays.
2.  Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
3.  We consider two pointers: `s_ptr` and `e_ptr` which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
4.  When considering a specific meeting pointed to by `s_ptr`, we check if this start timing is greater than the meeting pointed to by `e_ptr`. If this is the case then that would mean some meeting has ended by the time the meeting at `s_ptr` had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
5.  If a meeting has indeed ended i.e. if `start[s_ptr] >= end[e_ptr]`, then we increment `e_ptr`.
6.  Repeat this process until `s_ptr` processes all of the meetings.


<details>


```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
```

</details>

## 3. Parse latest Email

Write some code to parse out the latest reply in an email thread. Evaluating test cases one by one and adjusting your code as necessary. 
Great talking with you. Let's catchup soon.

Here is how a sample email might look like: 

```
Great talking with you. Let's catchup soon.

Thanks,
Mark Anderson
VP of Engineering
888-222-4444

On Fri, Nov 19, 2018 at 12:03 PM, Paul Johnson <paul@example.com> wrote:

> Let's talk at 11.
> Thanks
> Paul Johnson'''

```

#### 1. Approach that doesn't use Regex: 


<details>

```python
def parse_email_thread(email_thread):
    lines = email_thread.split('\n')
    top_message = ''
    latest_reply = ''
    signature = ''
    replies_started = False
    signature_started = False
    for line in lines:
        if "wrote:" in line:
            signature_started = False
            replies_started = True
        elif signature_started:
            signature = signature + line + '\n'
        elif replies_started:
            latest_reply = latest_reply + line + '\n'
        elif "Thanks," in line or "sincerely," in line:
            signature_started = True
        else:
            top_message = top_message + line + '\n'
    return signature

```

</details>


## 4. LRU Cache


Design a data structure that follows the constraints of a **[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

-   `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
-   `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
-   `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.
    
A grading rubric for an answer to the question "Design a data structure that implements LRU cache" could include the following criteria:

<details>

1.  Correctness: Does the solution correctly implement the LRU cache data structure with the ability to get and put elements, with a limit on the number of elements stored and with the property that the least recently used item is evicted when the cache is full?
2.  Time Complexity: Does the solution have an efficient time complexity, with constant-time operations for the get and put methods?
3.  Space Complexity: Does the solution have an efficient space complexity, using a constant amount of additional memory proportional to the number of elements stored in the cache?
4.  Code Quality: Does the solution have clean, readable, and well-commented code?
5.  Error Handling: Does the solution handle edge cases and exceptions correctly, such as if the cache is empty or if an element is not found in the cache?
6.  Test Cases: Does the solution include sufficient test cases to validate the correct behavior of the LRU cache, including cases for adding elements, removing elements, and updating elements?
7.  Optimization: Does the solution include any optimization techniques, such as using a doubly linked list or a hash map, to improve performance?   

</details>



