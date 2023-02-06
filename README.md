# daily-grokking
Daily Grokking Prep

- Task Scheduler 
- Find Median from Data Stream


# Task Scheduler

- https://www.youtube.com/watch?v=s8p8ukTyA2I

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return _the least number of units of times that the CPU will take to finish all the given tasks_.

**Example 1:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 2
**Output:** 8
**Explanation:** 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

**Example 2:**

**Input:** tasks = ["A","A","A","B","B","B"], n = 0
**Output:** 6
**Explanation:** On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

**Example 3:**

**Input:** tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
**Output:** 16
**Explanation:** 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A


```python

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
```


## Find Median from Data Stream

The **median** is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

-   For example, for `arr = [2,3,4]`, the median is `3`.
-   For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the MedianFinder class:

-   `MedianFinder()` initializes the `MedianFinder` object.
-   `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
-   `double findMedian()` returns the median of all elements so far. Answers within `10-5` of the actual answer will be accepted.

**Example 1:**

**Input**
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
**Output**
[null, null, null, 1.5, null, 2.0]

**Explanation**
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


```python

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2

```


```javascript

/** 
 * https://leetcode.com/problems/find-median-from-data-stream/
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */
class MedianFinder {
    constructor () {
        this.maxHeap = new MaxPriorityQueue()
        this.minHeap = new MinPriorityQueue()
    }

    /* Time O(log(N)) | Space (N) */
    insertNum (num) {
        this.addNum(num)
    }

    addNum (num, heap = this.getHeap(num)) {
        heap.enqueue(num)
        this.rebalance()
    }

    getHeap (num, { maxHeap, minHeap } = this) {
        const isFirst = maxHeap.isEmpty()
        const isGreater = num <= this.top(maxHeap);
        const isMaxHeap = (isFirst || isGreater);
        return (isMaxHeap)
            ? maxHeap
            : minHeap
    }

    rebalance ({ maxHeap, minHeap } = this) {
        const canShiftMax = (minHeap.size() + 1) < maxHeap.size()
        if (canShiftMax) return minHeap.enqueue(maxHeap.dequeue().element)

        const canShiftMin = maxHeap.size() < minHeap.size()
        if (canShiftMin) return maxHeap.enqueue(minHeap.dequeue().element)
    }

    /* Time O(1) | Space (1) */
    findMedian ({ maxHeap, minHeap } = this) {
        const isEven = maxHeap.size() === minHeap.size()
        return (isEven)
            ? this.average(maxHeap, minHeap)
            : this.top(maxHeap)
    }

    average (maxHeap, minHeap) {
        return (this.top(maxHeap) + this.top(minHeap)) / 2
    }

    top (heap) {
        return heap.front()?.element || 0
    }
}

```


