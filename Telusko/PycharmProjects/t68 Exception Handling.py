a = 5
b = 0

try:
    print('Resource open')
    print(a/b)
    k = int(input('Enyer a number: '))
    print(k)

except ZeroDivisionError as e:
    print('Hey, you cannot divide a Number by Zero')
    print('Error:', e)

except ValueError as e:
    print('Invalid input')
    print('Error:', e)

except Exception as e:
    print('Something went wrong...')

finally:
    print('Resource closed')

print('Bye')