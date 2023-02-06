1.  Hash - backed maps
```python 
#Define Dictionary
thisdict = {'bob': 7387, 'alice': 3719, 'jack': 7052}

#Get value by key
x = thisdict["bob"]

#Set value by key
thisdict["alice"] = 2456

#Print all keys
print(*thisdict.keys())

#Print all values
print(*thisdict.values())


a = [1, 2, 3] 
b = [4, 5, 6] 
c = [*a, *b] 

print(c)
[1, 2, 3, 4, 5, 6]

```

2. Queue
```python
from collections import deque

# Initializing a deque with maxlen
d = deque(maxlen=3)

# Adding elements to the deque
d.append(1)
d.appendleft(2)

# Removing elements from the deque
d.pop()
d.popleft()

# Checking the length of the deque
print(len(d))

# Checking if the deque is empty
print(not d)

# Iterating over the elements in the deque
for x in d:
    print(x)

# Accessing the first and last elements in the deque
print(d[0])
print(d[-1])
```

3. Stack
```python
# Approach 1
stack = [3, 4, 5]
stack.append(6)
stack.pop()

# Approach 2
stack = [3, 4, 5, 6]
stack = stack[:-1]

output -> [3, 4, 5]
```

4. Exceptions

```python
try:
   with open("testfile", "w") as fh:
       fh.write("This is my test file for exception handling!!")
except IOError as e:
   print(f"Error: {e}")
else:
   print("Written content in the file successfully")
finally:
   print("Code execution completed")

# Raise an exception
x = 10
if x > 5:
    raise ValueError(f'x should not exceed 5. The value of x was: {x}')

# Assert an error
import sys
assert 'linux' in sys.platform, "This code runs on Linux only."

```
7. Arithmetic

```python
# Modulus
result = 5 % 2
print(result) # 1

# Division (floating-point division)
result = 5 / 2
print(result) # 2.5

# Division (integer division)
result = 5 // 2
print(result) # 2

# Round (round to nearest whole number)
print(round(51.6)) # 52
print(round(51.5)) # 52
print(round(51.4)) # 51

# Round (round to specified decimal places)
print(round(2.665, 2)) # 2.67
print(round(2.676, 2)) # 2.68

# Floor (round down to nearest whole number)
import math
print(math.floor(300.16)) # 300
print(math.floor(300.76)) # 300

# Ceil (round up to nearest whole number)
print(math.ceil(300.16)) # 301
print(math.ceil(300.76)) # 301

```
8. 2-D Array

```python
# Approach 1

matrix = []
for i in range(rows):

  row = []  for j in range(cols):

    row.append(0)
  matrix.append(row)

# approach 2
matrix = [[0 for i in range(5)] for j in range(5)]

# approach 3
matrix = [[0] * cols for _ in range(rows)]
```


9. Sorting

```python
# Approach 1
sorted([5, 2, 3, 1, 4])

# Approach 2
a = [5, 2, 3, 1, 4]
a.sort()
```

11. Array Enumerate

```python
# iterate over array
ints = ["a", "b", "c"]

for idx, val in enumerate(ints):
    print(idx, val)
```
