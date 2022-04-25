class Student:

    school = 'Telusko'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is student class')


s1 = Student(32, 64, 98)
s2 = Student(38, 61, 45)

print(s1.avg())           # instance method
print(Student.getSchool())     # class method
Student.info()        # static method