def sumNnum(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return n + sumNnum(n - 1)
    
sum = sumNnum(11)
print('Sum of n natural number is',sum)