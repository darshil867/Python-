class computer:

    def __init__(self):
        self.name = 'Darshil'
        self.age = 19

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()

c1.update()
if c1.compare(c2):
    print('They are same')
else:
    print('They are different')

print(c1.name)
print(c2.name)

c2.name = 'Jayani'

print(c2.name)

print(id(c1))
print(id(c2))
