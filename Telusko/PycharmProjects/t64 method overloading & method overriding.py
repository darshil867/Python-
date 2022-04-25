# method overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):

        if a is not None and b is not None and c is not None:
            s = a + b + c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a

        return s

s1 = Student(34, 54)
print(s1.sum(3))

# method overriding
class A:

    def show(self):
        print('in A show')

class B(A):
    def show(self):
        print('in B show')

a1 = B()
a1.show()
