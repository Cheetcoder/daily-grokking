# Find Median From Data Stream

## Problem Statement

Design a class to calculate the median of a number stream. The class should have the following two methods:

1.  `insertNum(int num)`: stores the number in the class
2.  `findMedian()`: returns the median of all numbers inserted in the class

If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

**Example 1**:

```
1. insertNum(3)
2. insertNum(1)
3. findMedian() -> output: 2
4. insertNum(5)
5. findMedian() -> output: 3
6. insertNum(4)
7. findMedian() -> output: 3.5
```

## Try it yourself

Try solving this question here:


```python
from heapq import *  
  
  
class MedianOfAStream:  
  
  def insert_num(self, num):  
    # TODO: Write your code here  
    return  
  
  def find_median(self):  
    # TODO: Write your code here  
    return 0  
  
  
def main():  
  medianOfAStream = MedianOfAStream()  
  medianOfAStream.insert_num(3)  
  medianOfAStream.insert_num(1)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  medianOfAStream.insert_num(5)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  medianOfAStream.insert_num(4)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  
  
main()

```

## Solution

As we know, the median is the middle value in an ordered integer list. So a brute force solution could be to maintain a sorted list of all numbers inserted in the class so that we can efficiently return the median whenever required. Inserting a number in a sorted list will take O(N) time if there are ‘N’ numbers in the list. This insertion will be similar to the `Insertion sort`. Can we do better than this? Can we utilize the fact that we don’t need the fully sorted list - we are only interested in finding the middle element?

Assume ‘x’ is the median of a list. This means that half of the numbers in the list will be smaller than (or equal to) ‘x’ and half will be greater than (or equal to) ‘x’. This leads us to an approach where we can divide the list into two halves: one half to store all the smaller numbers (let’s call it `smallNumList`) and one half to store the larger numbers (let’s call it `largeNumList`). The median of all the numbers will either be the largest number in the `smallNumList` or the smallest number in the `largeNumList`. If the total number of elements is even, the median will be the average of these two numbers.

The best data structure that comes to mind to find the smallest or largest number among a list of numbers is a Heap. Let’s see how we can use a heap to find a better algorithm.

1.  We can store the first half of numbers (i.e., `smallNumList`) in a **Max Heap**. We should use a Max Heap as we are interested in knowing the largest number in the first half.
2.  We can store the second half of numbers (i.e., `largeNumList`) in a **Min Heap**, as we are interested in knowing the smallest number in the second half. Inserting a number in a heap will take O(logN), which is better than the brute force approach. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

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
  
  
def main():  
  medianOfAStream = MedianOfAStream()  
  medianOfAStream.insert_num(3)  
  medianOfAStream.insert_num(1)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  medianOfAStream.insert_num(5)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  medianOfAStream.insert_num(4)  
  print("The median is: " + str(medianOfAStream.find_median()))  
  
  
main()
```

If you had Issues with the above problem. Write it down 4 times! 



```python
```

```python
```

```python
```


```python
```
