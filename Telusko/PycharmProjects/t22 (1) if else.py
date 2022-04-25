x = int(input())
r = x % 2

if r == 0:
    print('Even')
    if x > 5:
        print('Great')
    else:
        print('Not so great')
else:
    print('Odd')

print('We learned if else')