f = lambda a: a * a

result = f(10)
print(result)

g = lambda a, b: a + b

result = g(3, 5)
print(result)

from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
doubles = list(map(lambda x: x * 2, evens))
sum = reduce(lambda a, b: a + b, doubles)
print(evens)
print(doubles)
print(sum)
