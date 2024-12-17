### Problem: **Binary Search for Closest Element**

You are tasked with implementing a function that performs a binary search to find the closest element to a target value in a sorted list of integers. If there are two numbers equidistant to the target, return the smaller number.

---

#### **Function Signature**
```python
def find_closest(nums: list[int], target: int) -> int:
    pass
```

---

### Requirements

1. **Input:**
   - `nums`: A list of integers in ascending order, e.g., `[1, 3, 5, 8, 12]`.
   - `target`: An integer to search for.

2. **Output:**
   - An integer representing the closest value to the target. 
   - If two numbers are equidistant, return the smaller number.

3. The function must have **O(log n)** time complexity.

---

### Example Usage
```python
# Example 1:
nums = [1, 3, 5, 8, 12]
target = 7
print(find_closest(nums, target))  # Output: 5

# Example 2:
nums = [2, 4, 6, 9]
target = 8
print(find_closest(nums, target))  # Output: 6

# Example 3:
nums = [10, 15, 20, 25]
target = 18
print(find_closest(nums, target))  # Output: 15

# Example 4:
nums = [1, 2, 3, 4, 5]
target = 5
print(find_closest(nums, target))  # Output: 5

# Example 5:
nums = [10, 20, 30]
target = 25
print(find_closest(nums, target))  # Output: 20
```

---

### Hints
1. Use binary search to efficiently narrow down the range of possible closest elements.
2. Keep track of the closest number during the search by comparing absolute differences with the target.
3. Consider edge cases:
   - If the target is smaller than all elements in `nums`, return the first element.
   - If the target is larger than all elements in `nums`, return the last element.
   - If two numbers are equidistant, return the smaller one.

---

This problem encourages you to apply binary search logic while handling additional conditions for closest-value comparison. It's a good exercise for improving both algorithmic thinking and Python proficiency!