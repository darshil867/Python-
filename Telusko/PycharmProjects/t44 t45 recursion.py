import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

i = 0
def greet():
    global i
    i += 1
    print('Hello ', i)
    greet()


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


x = int(input('Enter the number: '))
factorial = fact(x)
print(factorial)
# greet()