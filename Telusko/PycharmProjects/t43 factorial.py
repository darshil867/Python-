def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


x = int(input('Enter the number for finding factorial: '))
result = fact(x)
print(result)