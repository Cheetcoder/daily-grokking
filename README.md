# Daily Grokking Prep

## 1. Task Scheduler 
- [Task Scheduler Prompt](./problems/task_scheduler.md)
- [Python - Try it yourself](./practice/task_scheduler.py)

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

Hints: 
- You can use a Heap/Priority queue

## 2. Find median from Data stream

- [Find Median from Data Stream Prompt](./problems/Find_Median_From_Data_Stream.md)
- [Python - Try it yourself](./practice/find_median_data_stream.py)


Design a class to calculate the median of a number stream. The class should have the following two methods:

1.  `insertNum(int num)`: stores the number in the class
2.  `findMedian()`: returns the median of all numbers inserted in the class

Hints: 
- You can use a Heap/Priority queue (two of them)
_____________________

### Resources

- https://neetcode.io/practice - Many of the problems above can be found here, with video and code solultions
- https://replit.com/ - Real time collaboration to pair program
- https://obsidian.md/ - A markdown to take notes and help you practice without code formatting 