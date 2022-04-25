for i in range(5):
    for j in range(5):
        print('# ', end="")
    print()
print()

for i in range(5):
    for j in range(i + 1):
        print('# ', end="")
    print()
print()

for i in range(5):
    for j in range(5 - i):
        print('# ', end="")
    print()
print()

for i in range(5):
    for j in range(5 - i):
        print(j + i + 1, end=" ")
    print()
print()

a, b = "ABCD", "PQR"
for i in range(4):
    print(a[:i+1] + b[i:])