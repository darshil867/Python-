def greet():
    print('Hello')
    print('Good Morning')


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


greet()
result1, result2 = add_sub(3, 4)
print(result1, result2)
print()


def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print('x ', lst)


lst = [10, 20, 30]
print(id(lst))
update(lst)
print('lst ', lst)
print()


def update1(x):
    print(id(x))
    x = 25
    print(id(x))
    print('x ', x)


a = 3
print(id(a))
update1(a)
print('a ', a)


def person(name, age=18):  # default
    print(name)
    print(age)


age = 22
person('Darshil', age)  # position
person(name='Darshil', age=19)  # keyword
print()


def sum(a, *b):    # you can start from c = 0 means def sum(*b)
    c = a          # variable length
    for i in b:
        c = c + i
    print(c)


sum(3, 5, 5, 3)


def person(name, **data):          # keyworded variable length argument
    print(name)
    for i, j in data.items():
        print(i, j)


person('Darshil', age=18, city='la', mob=9893)
print()

a = 10
def something():
    a = 25
    print('In fun ', a)


something()
print('Outside ', a)
print()

a = 10
def something():
    global a
    a = 15
    print('In fun ', a)


something()
print('Outside ', a)
print()

a = 10
print(id(a))
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print(x)
    print('In fun ', a)
    globals()['a'] = 12


something()
print('Outside ', a)