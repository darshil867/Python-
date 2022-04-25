def pattern(n):
    for i in range(n):
        for j in range(n - i):
            print('*', end='')
        print()
    print()

reverseTrianglePattern = pattern(3)
print(reverseTrianglePattern)

def printPattern(n):
    for i in range(n): 
        print("* " * (n-i)) 

printPattern(5) 
