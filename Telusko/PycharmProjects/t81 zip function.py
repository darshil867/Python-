names = ('navin', 'kiran', 'harsh')
comps = ('dell', 'apple', 'ms')

zipped = list(zip(names, comps))
print(zipped)

for (a, b) in zipped:
    print(a, b)
