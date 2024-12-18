def findClosest(arr: list[int], target: int) -> int:
    if not arr:
        raise ValueError("The input list cannot be empty.")
    if target < arr[0]:
        return arr[0]
    if target > arr[-1]:
        return arr[-1]
    
    left, right = 0, len(arr) - 1
    closest = arr[0]
    
    while left <= right:
        mid = (left+right) // 2
        
        print("Old Closest: ",closest)
        print("arr[mid]: ", arr[mid])
        print("Target: ", target)
        if abs(arr[mid] - target) < abs(closest - target) or \
            abs(arr[mid]) - target == abs(closest - target) and arr[mid] < closest:
            print("abs(arr[mid] - target): ",abs(arr[mid] - target))
            print("abs(closest - target): ",abs(closest - target))
            print("Closest: ",closest)
            closest =  arr[mid]
            
        
            
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return arr[mid]
        
    return closest

# Test Cases
nums = [1, 3, 5, 8, 12]
target = 7
print(findClosest(nums, target))  # Output: 8

nums = [2, 4, 6, 9]
target = 8
print(findClosest(nums, target))  # Output: 9

nums = [10, 15, 20, 25]
target = 18
print(findClosest(nums, target))  # Output: 20

nums = [1, 2, 3, 4, 5]
target = 5
print(findClosest(nums, target))  # Output: 5

nums = [10, 20, 30]
target = 25
print(findClosest(nums, target))  # Output: 20
