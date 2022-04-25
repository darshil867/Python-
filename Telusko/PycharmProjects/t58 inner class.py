class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Darshil', 14)
s2 = Student('Pratham', 35)

# print(s1.name, s1.rollno)
s1.show()

# print(s1.lap.brand)

lap1 = Student.Laptop()
lap2 = Student.Laptop()

print(lap1.brand)

# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))