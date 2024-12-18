import random
import time
from tqdm import tqdm

def optimizedBubbleSort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    startTime = time.time_ns()
    
    for i in tqdm(range(n)):
        swapped = False
        
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if i % 10 == 0:
            print(f"Iteration {i}/{n} - Comparison: {comparisons} - Swaps: {swaps}")        
        
        if not swapped:
            break
        
    endTime = time.time_ns()
    
    timeTaken = (endTime - startTime)
    return arr, timeTaken, comparisons, swaps

arr = [64, 34, 25, 12, 22, 11, 90]
sortedArray, timeTaken, comparisons, swaps = optimizedBubbleSort(arr)

print("Sorted Array: ", sortedArray)
print("Time Takem: ", timeTaken)
print("Comparisons: ", comparisons)
print("Swaps: ", swaps)
                

largeArr = [random.randint(1, 1000) for _ in range(1000000)]
sortedArray_Large, timeTaken_Large, comparisons_Large, swaps_Large = optimizedBubbleSort(largeArr)

print("Sorted Array _Large: ", sortedArray_Large)
print("Time Takem _Large: ", timeTaken_Large)
print("Comparisons _Large: ", comparisons_Large)
print("Swaps _Large: ", swaps_Large)    
    