from typing import List, Dict, Union

def insertionSort_Custom(arr: List[Dict[str, Union[str, int]]]):
    def compareDictionaries(comparer: Dict[str, Union[str, int]], current: Dict[str, Union[str, int]]) -> bool:
        if comparer["name"] != current["name"]: 
            return str(comparer["name"]) > str(current["name"])
        if comparer["age"] != current["age"]:
            return int(comparer["age"]) > int(current["age"])
        return int(comparer["score"]) < int(current["score"])
    
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        
        while j >= 0 and compareDictionaries(arr[j], current):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
        
    return arr
            
data = [
    {"name": "Alice", "age": 30, "score": 85},
    {"name": "Bob", "age": 25, "score": 95},
    {"name": "Alice", "age": 25, "score": 90},
    {"name": "Bob", "age": 30, "score": 70},
    {"name": "Alice", "age": 30, "score": 75}
]

sorted_data = insertionSort_Custom(data)
print(sorted_data)
