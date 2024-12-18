### Python Interpolation Search Challenge: 

#### **Problem Description:**
You are tasked with implementing a robust **interpolation search algorithm** in Python. The function must find the index of a target element in a **sorted list**. If the target does not exist in the list, return `-1`. Your implementation must efficiently handle edge cases, such as when the target is outside the bounds of the list or when duplicate values are present.

#### **Function Signature:**
```python
def interpolation_search(arr: list[int], target: int) -> int:
    """
    Perform interpolation search on a sorted list to find the index of a target.

    :param arr: A sorted list of integers.
    :param target: The integer value to search for.
    :return: The index of the target in the list, or -1 if not found.
    """
```

---

#### **Example Usage:**
```python
# Example 1
arr = [10, 12, 15, 19, 23, 29, 35, 42]
target = 23
print(interpolation_search(arr, target))  # Output: 4

# Example 2
arr = [5, 7, 7, 8, 10, 15, 20, 25]
target = 7
print(interpolation_search(arr, target))  # Output: 1 or 2 (any valid index is acceptable)

# Example 3
arr = [2, 4, 8, 16, 32, 64]
target = 5
print(interpolation_search(arr, target))  # Output: -1
```

---

#### **Requirements:**
1. **Input Validation**: 
   - Ensure the input list `arr` is sorted in ascending order.
   - Return `-1` immediately for an empty list.
2. **Edge Cases**: 
   - Handle cases where the target is smaller than the smallest element or larger than the largest element in the list.
   - Handle lists with duplicate values.
3. **Efficiency**: 
   - Use the formula:  
     ```python
     pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
     ```
     to calculate the probable position.
   - Adjust the search range (`low` and `high`) based on comparisons with the `target`.
4. **Return Value**:
   - Return the index of the `target` if found.
   - Return `-1` if the `target` is not in the list.

---

#### **Hints:**
1. **Formula Validation**: Ensure the denominator `(arr[high] - arr[low])` is not zero to avoid a division error. This situation arises when all elements in the range are identical.
2. **Bounds Check**: Before accessing `arr[pos]`, ensure that `pos` is within the valid range (`low <= pos <= high`) to prevent index errors.
3. **Efficiency**: The algorithm works best for uniformly distributed data. If the data is skewed, the performance might degrade closer to a linear search.
4. **Iterative or Recursive**: While implementing, decide whether an iterative or recursive approach suits your needs better. Iterative implementations often avoid stack overflow in Python for deep recursion.

