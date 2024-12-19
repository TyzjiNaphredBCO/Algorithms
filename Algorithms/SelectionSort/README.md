### **Problem Title:**  
**Optimized Selection Sort for Large Data Sets**

---

### **Problem Description:**  
You are tasked to implement a modified **Selection Sort** that operates efficiently on large datasets with the following properties:  
1. The dataset is divided into two halves: the first half is almost sorted, and the second half is randomly shuffled.  
2. Instead of sorting the dataset in one pass, the algorithm must:  
   - Fully sort the first half using **Selection Sort**.  
   - Rearrange the second half by **moving the smallest values to the beginning** of this half without fully sorting it.

The program should return a single sorted list where the first half is in ascending order, and the second half has its smallest values grouped at the start (but not necessarily sorted).

---

### **Requirements:**  
1. You **must use Selection Sort** for the fully sorted part (first half).  
2. Use a modified Selection Sort for the second half to move the smallest values to the front.  
3. The code should handle datasets up to **1 million elements** efficiently.  
4. The function should take the following inputs:  
   - `data`: A list of integers.  
   - `split_index`: An integer denoting the index that divides the first and second halves.  

5. The output should be a single list where:
   - The first `split_index` elements are sorted.
   - The rest of the elements are grouped with smaller values at the start.

---

### **Example Usage:**  
#### **Input:**  
```python
data = [10, 8, 7, 12, 15, 4, 9, 11, 20, 25, 1, 6, 3]
splitIndex = 7
groupSize = 4
```

#### **Output:**  
```python
[4, 7, 8, 9, 10, 12, 15, 1, 3, 6, 11, 25, 20]
```

#### **Explanation:**  
1. The first 7 elements (`data[:split_index]`): `[10, 8, 7, 12, 15, 4, 9]` are fully sorted: `[4, 7, 8, 9, 10, 12, 15]`.  
2. The rest (`data[split_index:]`): `[20, 25, 1, 6, 3]` are grouped with smaller values at the start: `[1, 3, 6, 11, 25, 20]`.

---

### **Hints:**  
1. Implement a helper function for standard Selection Sort.  
2. For the second half, adapt the Selection Sort to find and move the smallest element to the current position iteratively without fully sorting.  
3. Use slicing (`data[:split_index]`, `data[split_index:]`) to work on subsets.  
4. Be mindful of time complexity—use optimizations where possible.  
5. Test your algorithm on datasets of varying sizes to ensure it scales effectively.  
