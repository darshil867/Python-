from array import *

arr = array('i', [1, 2, 3, 4, 5])

for i in range(5):
    if i == 2:
        continue
    else:
        print(arr[i], end=" ")