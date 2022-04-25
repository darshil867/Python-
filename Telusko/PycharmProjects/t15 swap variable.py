a = 5
b = 6

a, b = b, a

print(a)
print(b)

temp = a
a = b
b = temp

print(a)
print(b)

a = a + b
b = a - b
a = a - b

print(a)
print(b)

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)
