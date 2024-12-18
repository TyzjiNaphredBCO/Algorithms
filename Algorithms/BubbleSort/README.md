### Problem: **Optimized Bubble Sort for Large Data Sets**

#### Question:
You are tasked with implementing an **optimized bubble sort** for an extremely large list of numbers (up to 1 million elements). The challenge is not only to implement the sorting algorithm but also to enhance the algorithm to reduce unnecessary comparisons during the sorting process, optimizing the algorithm to handle large data sets efficiently.

**You need to implement the following in Python:**

1. **Bubble Sort Algorithm**: Implement a bubble sort algorithm where the outer loop reduces in size as the algorithm progresses. Additionally, stop the sorting early if no swaps were made during a pass (i.e., the list is already sorted).
   
2. **Performance Evaluation**: Since the list can contain up to 1 million elements, evaluate the performance (in terms of time complexity and number of comparisons/swaps) of your implementation. Output the time taken and the total number of comparisons and swaps made for sorting the array.

3. **Input and Output Format**:
    - Input: A list of integers, `arr`, that can contain up to 1 million integers.
    - Output: A sorted list of integers.
    - Along with the sorted list, output the following:
        - Time taken to sort the list (in seconds).
        - The total number of comparisons and swaps performed.

---

#### Example Usage:

**Input:**

```python
arr = [64, 34, 25, 12, 22, 11, 90]
```

**Output:**

```python
Sorted Array: [11, 12, 22, 25, 34, 64, 90]
Time Taken: 0.0003 seconds
Comparisons: 28
Swaps: 19
```

---

#### Requirements:

1. **Bubble Sort Optimization**: Implement the bubble sort in such a way that it reduces the number of iterations as much as possible. You should stop the algorithm early if no swaps occur in a full pass over the list.

2. **Time Complexity**: Your algorithm should ideally aim to reduce the number of comparisons and swaps, aiming for an average case of O(n²) time complexity. However, it's crucial to note that bubble sort is inherently inefficient for large datasets, so make sure to demonstrate optimizations.

3. **Handling Large Data Sets**: The input list can have up to 1 million elements, so ensure the code runs efficiently for large inputs. You can use the `random` module to generate large test cases.

4. **Performance Metrics**: Record the time taken to sort the list using the `time` module. Track the total comparisons and swaps performed during the sorting process.

---

#### Hints:

- **Early Stopping Optimization**: After each pass, if no swaps were made, you can break out of the loop early, as the list is already sorted.
- **Tracking Comparisons and Swaps**: Use two counters to track the total number of comparisons and swaps. Each time a comparison is made, increment the comparisons counter. Each time a swap occurs, increment the swaps counter.
- **Edge Cases**: Handle edge cases where the list might already be sorted or contain only one element. You can skip unnecessary sorting in these cases.
- **Large Data Handling**: Use random number generation (`random.randint()`) to generate large datasets for testing. Also, ensure that the code works with different list sizes, including edge cases like an empty list or a list of length 1.