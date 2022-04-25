# from array import ArrayType

from array import *

arr = array('i', [1, 2, 3, 4, 5])

for i in range(len(arr)//2):
    temp = arr[i]
    arr[i] = arr[len(arr) - i - 1]
    arr[len(arr) - i - 1] = temp
print(arr)