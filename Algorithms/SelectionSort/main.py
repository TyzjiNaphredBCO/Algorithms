import random
import time
from tqdm import tqdm

def selectionSort(data):
    n = len(data)
    
    for i in tqdm(range(n)):
        minIndex = i
        for j in range(i + 1, n):
            if data[j] < data[minIndex]:
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]
        
def selectionSort_Modified(data, groupSize):
    n = len(data)
    
    for i in tqdm(range(groupSize)):
        minIndex = i
        for j in range(i + 1, n):
            if data[j] < data[minIndex]:
                minIndex = j
        data[i], data[minIndex] = data[minIndex], data[i]
        
def selectionSort_Hybrid(data, splitIndex, groupSize):
    startTime = time.time()
    
    firstHalf = data[:splitIndex]
    secondHalf = data[splitIndex:]
    
    selectionSort(firstHalf)
    selectionSort_Modified(secondHalf, groupSize)
    
    endTime = time.time()
    
    elapseTime = endTime - startTime
    print(f"Elapsed Time: {elapseTime}")
    
    return firstHalf + secondHalf

data = [10, 8, 7, 12, 15, 4, 9, 11, 20, 25, 1, 6, 3]
splitIndex = 7
groupSize = 4
result = selectionSort_Hybrid(data, splitIndex, groupSize)
print("Sorted Output: ", result)

data_Big = [random.randint(1, 1000) for _ in range(1000000)]
splitIndex = 7
groupSize = 4
result = selectionSort_Hybrid(data_Big, splitIndex, groupSize)
print("Sorted Output: ", result)