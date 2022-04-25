from array import *

arr = array('i', [])

n = int(input('Enter the length of array: '))

for i in range(n):
    a = int(input('Enter the next element of array: '))
    arr.append(a)
print(arr)

val = int(input('Enter the value for search: '))

k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

print(arr.index(val))