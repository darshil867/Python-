n = int(input('Enter a number for print series upto n: '))

for j in range(1, n + 1):
    for i in range(2, j):  # 0r for i in range(2, int(sqrt(n) + 1)):

        if j % i == 0:
            break
    else:
        print(f'Prime Number: {j}')