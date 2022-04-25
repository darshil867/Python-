x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print('x is greatest')
elif y > z and y > x:
    print('y is greatest')
else:
    print('z is greatest')