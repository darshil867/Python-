def count(lst):

    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


lst = [12, 13, 14, 15, 16, 17, 18, 19, 20]
even, odd = count(lst)

print('Even : {} and Odd : {}'.format(even, odd))
print(f'Even : {even} and Odd : {odd}')
