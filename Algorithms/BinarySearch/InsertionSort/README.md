### Extreme Python Problem: Advanced Insertion Sort with Complex Constraints

---

#### **Problem Statement**
You are tasked with implementing a custom insertion sort algorithm to sort a list of dictionaries based on multiple keys in a specific order. The keys are `"name"`, `"age"`, and `"score"`. The sorting must adhere to the following rules:

1. **Primary Key**: Sort by `"name"` in ascending alphabetical order.
2. **Secondary Key**: If two names are identical, sort by `"age"` in ascending numerical order.
3. **Tertiary Key**: If both name and age are identical, sort by `"score"` in descending numerical order.

Your implementation should not use any built-in sorting functions like `sorted()` or `.sort()`. It must adhere strictly to the insertion sort algorithm, manually comparing and inserting elements.

---

#### **Requirements**
1. The input will be a list of dictionaries, where each dictionary contains the keys `"name"`, `"age"`, and `"score"`. Example:
   ```python
   [
       {"name": "Alice", "age": 30, "score": 85},
       {"name": "Bob", "age": 25, "score": 95},
       {"name": "Alice", "age": 25, "score": 90}
   ]
   ```
2. The function can be named `custom_insertion_sort(data: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]`.

3. You are allowed to use basic list operations (`append()`, `pop()`, `insert()`) and comparison operators.

4. The function must have a time complexity of \(O(n^2)\) due to the insertion sort constraint.

5. Input validation is **not required**. Assume the input is always well-formed.

---

#### **Function Signature**
```python
def custom_insertion_sort(data: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]:
    pass
```

---

#### **Example Usage**

```python
data = [
    {"name": "Alice", "age": 30, "score": 85},
    {"name": "Bob", "age": 25, "score": 95},
    {"name": "Alice", "age": 25, "score": 90},
    {"name": "Bob", "age": 30, "score": 70},
    {"name": "Alice", "age": 30, "score": 75}
]

sorted_data = custom_insertion_sort(data)
print(sorted_data)
```

**Expected Output**:
```python
[
    {'name': 'Alice', 'age': 25, 'score': 90}, 
    {'name': 'Alice', 'age': 30, 'score': 85}, 
    {'name': 'Alice', 'age': 30, 'score': 75}, 
    {'name': 'Bob', 'age': 25, 'score': 95}, 
    {'name': 'Bob', 'age': 30, 'score': 70}
]
```

---

#### **Hints**
1. Implement a comparison helper function to evaluate the priority of two dictionaries based on the given keys.
2. Use a nested loop where the outer loop iterates over the input list, and the inner loop finds the correct position for the current element.
3. Think about how to handle comparisons for ascending and descending orders within the helper function.
4. Visualize the insertion process to debug edge cases, such as ties between all three keys.

Good luck!