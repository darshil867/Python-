a = 34
b = 3
c = 89
d = 734

if a > b:
    maxNum1 = a
else:
    maxNum1 = b

if c > d:
    maxNum2 = c
else:
    maxNum2 = d

if maxNum2 > maxNum1:
    maxNum = maxNum2
else:
    maxNum = maxNum1

print('Maximum number out of these four number is', maxNum)