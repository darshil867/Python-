class A:

    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1-A is working')

    def feature2(self):
        print('feature 2 is working')

class B:

    def __init__(self):
        super().__init__()
        print('in B init')

    def feature1(self):
        print('feature 1-B is working')

    def feature4(self):
        print('feature 4 is working')

class C(A, B):

    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2()

a1 = C()
a1.feature1()
a1.feat()