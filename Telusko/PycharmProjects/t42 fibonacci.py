def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a, end=' ')
        print(b, end=' ')
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c, end=' ')


n = int(input('Enter a number: '))
if n > 0:
    fib(n)
else:
    print("You entered wrong value (negative value)")
print()


def fibo(n):
    a = 0
    b = 1
    print(a, end=' ')
    print(b, end=' ')
    if n < 0:
        print("invalid value enter a valid one!")
    else:
        for i in range(2, n):  # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a + b
            a = b
            b = c
            if c <= n:
                print(c, end=' ')


x = int(input("Enter till how many numbers you want fibonacci series = "))
fibo(x)
