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
        
        if ()