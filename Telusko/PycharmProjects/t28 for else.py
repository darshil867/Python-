nums = [11, 16, 18, 28, 27]

for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print('Not Found')