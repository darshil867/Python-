from numpy import *

arr = array([1, 2, 3, 4, 5])
print(arr)
arr = array([1, 2, 3, 4, 5], int)
print(arr)
print(arr.dtype)
print()

arr = array([1, 2, 3, 4, 5.0])
print(arr.dtype)
print(arr)
print()

arr = array([1, 2, 3, 4, 5], float)
print(arr.dtype)
print(arr)
print()

arr = linspace(0, 16, 10)
print(arr)
print()

arr = linspace(0, 15, 16)
print(arr)
print()

arr = linspace(0, 16, 20)
print(arr)
print()

arr = linspace(0, 15)
print(arr)
print()

arr = arange(1, 15, 2)
print(arr)
print()

arr = logspace(1, 40, 5)
print(arr)
print('%.2f' % arr[0])
print('%.2f' % arr[4])
print()

arr = zeros(10)
print(arr)
arr = zeros(10, int)
print(arr)
print()

arr = ones(10)
print(arr)
arr = ones(10, int)
print(arr)
print()

arr = array([1, 2, 3, 4, 5])
arr = arr + 4
print(arr)
print()

arr1 = array([1, 2, 3, 4, 5])
arr2 = array([1, 2, 3, 4, 5])
arr3 = arr1 + arr2
print(arr3)
print(concatenate([arr1, arr2]))
print()

arr = array([5, 4, 3, 3, 2, 1])
print(sin(arr))
print(cos(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(max(arr))
print(min(arr))
print(unique(arr))
print(sort(arr))
print()

arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
print()

arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.view()
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))
print()

arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.view()
arr1[1] = 9
print(arr1)    # SHALLOW COPY
print(arr2)
print(id(arr1))
print(id(arr2))
print()

arr1 = array([1, 2, 3, 4, 5])
arr2 = arr1.copy()
arr1[4] = 4
print(arr1)    # DEEP COPY
print(arr2)
print(id(arr1))
print(id(arr2))
print()