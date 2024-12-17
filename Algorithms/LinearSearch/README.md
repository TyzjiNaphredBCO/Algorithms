### Problem: Linear Search in Python - Finding the First Occurrence

#### Question:
Write a Python function `linear_search` that takes a list of integers and a target integer as input. The function should return the index of the first occurrence of the target in the list. If the target is not found, the function should return `-1`.

#### Example Usage:
```python
# Example 1
numbers = [5, 3, 7, 9, 3, 2, 1]
target = 3
result = linear_search(numbers, target)
print(result)  # Output: 1

# Example 2
numbers = [10, 15, 20, 25]
target = 5
result = linear_search(numbers, target)
print(result)  # Output: -1
```

#### Requirements:
1. Your function must use a **linear search algorithm**, meaning it should iterate through the list from the start to the end.
2. Do **not** use Python's built-in methods like `.index()` to solve this problem.
3. The function must have the following signature:
   ```python
   def linear_search(numbers: list[int], target: int) -> int:
   ```

#### Hints:
1. Use a loop to traverse the list, comparing each element with the target.
2. Once you find the target, return the index of that element.
3. If the loop completes without finding the target, return `-1`. 
4. Consider edge cases like an empty list or a list with duplicate elements.

#### Bonus:
Write a second version of the function, `linear_search_all`, that returns a list of all indices where the target occurs. If the target is not found, return an empty list.

#### Example for Bonus:
```python
# Example
numbers = [5, 3, 7, 9, 3, 2, 1]
target = 3
result = linear_search_all(numbers, target)
print(result)  # Output: [1, 4]
```

