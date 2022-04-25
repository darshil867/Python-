nums = [23,43,54,67,24]
nums[0]
23

nums[43]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    nums[43]
IndexError: list index out of range

nums[4]
24
nums[-1]
24
nums[-2:]
[67, 24]
nums[2:]
[54, 67, 24]
nums[-5]
23
 
names = ['Darshil', 'Tejas', 'Navin']
names
['Darshil', 'Tejas', 'Navin']

values = [9.4, 'Darshil', 5]
values
[9.4, 'Darshil', 5]

mil = [nums, names]
mil
[[23, 43, 54, 67, 24], ['Darshil', 'Tejas', 'Navin']]
 
nums.append(45)
nums
[23, 43, 54, 67, 24, 45]

nums.clear
<built-in method clear of list object at 0x0000020BD1627400>
nums.clear()
nums
[]

nums = [23,43,54,67,24]
nums.insert(2,44)
nums
[23, 43, 44, 54, 67, 24]

nums.remove(67)
nums
[23, 43, 44, 54, 24]

nums.pop(1)
43
nums
[23, 44, 54, 24]
nums.pop()
24
nums
[23, 44, 54]

del nums[2:]
nums
[23, 44]

nums.extend([29, 86, 35, 80])
nums
[23, 44, 29, 86, 35, 80]
min(nums)
23
max(nums)
86
sum(nums)
297
nums.sort()
nums
[23, 29, 35, 44, 80, 86]