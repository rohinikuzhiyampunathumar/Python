from numpy import *
arr = array([
    [1,2,3,9,8,7],
    [4,5,6,1,2,3]
])
print(arr.shape)
print(arr.dtype)
print(arr.ndim)
print(arr.size)
arr1 = arr.flatten()
arr2 = arr1.reshape(2,2,3)
print(arr2)
arr3 = array([
    [1,2,3],
    [4,5,6]
])
m= matrix(arr3)

