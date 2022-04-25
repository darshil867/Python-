from numpy import *

arr1 = array([
    [1, 2, 3, 4, 4, 3],
    [5, 6, 7, 8, 3, 9]
])

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)
print()

arr3 = arr2.reshape(3, 4)
print(arr3)
print()

arr3 = arr2.reshape(2, 2, 3)
print(arr3)
print()

arr1 = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
m = matrix(arr1)
print(m)
print()

m = matrix('1,2,3,4 ; 1,2,3,4')
print(m)
print()

m = matrix('1,2 ; 3,4 ; 1,2 ; 3,4')
print(m)
print()

m = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
print(m)
print()
print(diagonal(m))
print()
print(m.max())
print()
print(m.min())
print()

m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m3 = m1 + m2
print(m3)
print()
m3 = m1 * m2
print(m3)
print()

from numpy import *
arr = array([1, 2, 3, 4, 25])
arr1 = array([15, 16, 20, 21, 5])
for i in range(len(arr1)):
    arr[i] = arr[i] + arr1[i]
print(arr)
print()

from array import *
arr = array('l', [4, 5, 634, 7])

if arr[1] > arr[0]:
    greater1 = arr[1]
else:
    greater1 = arr[0]
if arr[2] > arr[3]:
    greater2 = arr[2]
else:
    greater2 = arr[3]
if greater2 > greater1:
    greater = greater2
else:
    greater = greater1

print(f'Greatest number of this array is {greater}')
                