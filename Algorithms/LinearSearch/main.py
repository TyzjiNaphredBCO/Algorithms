def linearSearch(arr: list[int], target: int) -> int:
    for index in range(len(arr)):
        if arr[index] == target:
            print('Data found in index: %d'%index)
            return index
    print('Data not found in index')
    raise ValueError("Data not found in index")

arr1 = [10, 20, 30, 40, 50]
target1 = 30
target1Index = linearSearch(arr1, target1)
print(target1Index)

arr2 = [3, 6, 9, 12, 15]
target2 = 18
target2Index = linearSearch(arr2, target2)
print(target2Index)

def linearSearchAll(arr: list[int], target: int) -> list[int]:
    indices = []
    for index in range(len(arr)):
        if arr[index] == target:
            indices.append(arr[index])
    if len(indices) > 0:
        print("Number of data found: %d" % (len(indices)))
        return indices
    else:
        print("No data found.")
        raise ValueError("No data found.")
    
arr3 = [5, 3, 7, 9, 3, 2, 1]
target3 = 3
target3Indices = linearSearchAll(arr3, target3)
print(target3Indices)