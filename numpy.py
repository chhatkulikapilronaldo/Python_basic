import numpy as np

# Introduction: Importing NumPy

# Array Creation
# Creating a 1D array from a list
array1 = np.array([1, 2, 3, 4, 5])

# Creating a 2D array (matrix)
array2 = np.array([[1, 2, 3], [4, 5, 6]])

# Creating arrays of zeros, ones, and a range of numbers
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
range_array = np.arange(10)

# Dimensions
# 1D array
print("1D array shape:", array1.shape)

# 2D array
print("2D array shape:", array2.shape)

# 3D array
array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D array shape:", array3.shape)

# Data Types
# Creating an array with a specific data type
array_float = np.array([1, 2, 3], dtype=np.float64)
print("Array data type:", array_float.dtype)

# Array Attributes
array = np.array([[1, 2, 3], [4, 5, 6]])
print("Number of dimensions:", array.ndim)
print("Shape of the array:", array.shape)
print("Total number of elements:", array.size)
print("Data type of elements:", array.dtype)

# Indexing and Slicing
# Indexing
print("First element of array1:", array1[0])

# Slicing
print("Elements from index 1 to 4 in array1:", array1[1:4])

# 2D array indexing and slicing
print("Element at row 0, column 1 in array2:", array2[0, 1])
print("All elements in column 1 of array2:", array2[:, 1])
print("All elements in row 1 of array2:", array2[1, :])

# Array Copy and View
# View (shallow copy)
view = array1.view()
view[0] = 10
print("Original array after view modification:", array1)
print("View array:", view)

# Copy (deep copy)
copy = array1.copy()
copy[0] = 20
print("Original array after copy modification:", array1)
print("Copy array:", copy)

# Creating Array from Numerical Range
# Using arange()
array_range = np.arange(0, 10, 2)
print("Array using arange:", array_range)

# Using linspace()
array_linspace = np.linspace(0, 10, 5)
print("Array using linspace:", array_linspace)

# Array Broadcasting
array_broadcast = np.array([1, 2, 3])
array2_broadcast = np.array([[1], [2], [3]])

# Broadcasting the smaller array to the shape of the larger array
result = array_broadcast + array2_broadcast
print("Broadcasted array:\n", result)

# Iterating Over Arrays
# Iterating over rows
print("Iterating over rows of array2:")
for row in array2:
    print(row)

# Iterating over each element
print("Iterating over each element of array2:")
for element in array2.flat:
    print(element)

# Sorting and Searching
array_sort_search = np.array([3, 1, 2])

# Sorting
sorted_array = np.sort(array_sort_search)
print("Sorted array:", sorted_array)

# Searching
index = np.where(array_sort_search == 2)
print("Index of element '2' in array_sort_search:", index)

# Statistical Functions
array_stat = np.array([1, 2, 3, 4, 5])

# Mean
mean = np.mean(array_stat)
print("Mean of array_stat:", mean)

# Median
median = np.median(array_stat)
print("Median of array_stat:", median)

# Standard Deviation
std_dev = np.std(array_stat)
print("Standard Deviation of array_stat:", std_dev)

# Sum
total_sum = np.sum(array_stat)
print("Sum of elements in array_stat:", total_sum)

# Minimum and Maximum
min_val = np.min(array_stat)
max_val = np.max(array_stat)
print("Minimum value in array_stat:", min_val)
print("Maximum value in array_stat:", max_val)
