from array import *

vals = array('i', [1, -2, 3, -4, 5])
print(vals)
print(vals.typecode)
print(vals.buffer_info())
vals.reverse()
print(vals)
print(vals[1])
print()
for i in range(len(vals)):
    print(vals[i])
print()

for i in vals:
    print(i)
print()

newArr = array(vals.typecode, (a for a in vals))
for i in newArr:
    print(i)
print()

newArr = array(vals.typecode, (a*a for a in vals))
for i in newArr:
    print(i)
print()

i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1

"""     i = signed int
        I = unsigned int
        l = signed long (int)
        L = unsigned long (int)
        f = float
        d = double (float)
        b = signed char (int)
        B = unsigned char (int)
        u = unicode character    """