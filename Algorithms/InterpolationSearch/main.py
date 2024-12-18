def interpolationSearch(arr: list[int], target: int) -> int:
    if not arr:
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if arr[left] == arr[right]:
            if arr[left] == target:
                return left
            else:
                return -1
            
        probe = left + (target - arr[left]) // (arr[right] - arr[left]) * (right - left)

        if arr[probe] == target:
            return probe
        elif arr[probe] < target:
            left = probe + 1
        else:
            right = probe - 1
            
    return -1

arr = [10, 12, 15, 19, 23, 29, 35, 42]
target = 23
print(interpolationSearch(arr, target))

arr = [5, 7, 7, 8, 10, 15, 20, 25]
target = 7
print(interpolationSearch(arr, target))

arr = [2, 4, 8, 16, 32, 64]
target = 5
print(interpolationSearch(arr, target))