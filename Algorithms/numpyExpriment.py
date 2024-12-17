import numpy as np

arr = np.array([1,2,3,4,5])

sum_arr = np.sum(arr)
mean_arr = np.mean(arr)
std_arr = np.std(arr)

print("Array: ", arr)
print("Sum of elements: ", sum_arr)
print("Mean of elements: ", mean_arr)
print("Standard Deviation of elements: ", std_arr)

matrix = np.matrix([[1,2],[3,4],[5,6]])

matrix_mul = np.dot(matrix.T, matrix)

print("\nMatrix:\n", matrix)
print("\nMatrix after multiplcation (Matrix.T * Matrix):\n", matrix_mul)