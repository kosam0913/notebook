# LRU Cache

1. use extra data structure: ListNode
2. breakdown chunk: move_to_head() > remove_node() then add node()

```python
class ListNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        
        self.prev = None # ListNode
        self.next = None # ListNode
```

# First Missing Positive

1. O(3n) = O(n)
2. Can use posigive or negative represent existance
3. Analyze first, no rush

```python
n = len(nums)
result = n + 1

# Step 1: Replace non-positive integers with n + 1
for i, num in enumerate(nums):
    if num <= 0:
        nums[i] = n + 1

# Step 2: Mark the presence of positive integers by negating the value at index num - 1
for num in nums:
    num = abs(num)
    if 1 <= num <= n:
        nums[num - 1] = -abs(nums[num - 1])

# Step 3: Find the smallest missing positive integer
for i, num in enumerate(nums):
    if num > 0:
        result = min(result, i + 1)
```
