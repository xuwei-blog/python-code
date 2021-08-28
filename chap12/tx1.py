class Student:
    native_place='jl'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print('xszcf')

    @staticmethod
    def method():
        print('jtff')

    @classmethod
    def cm(cls):
        print('lff')

stu1 = Student('张三',20)

print(stu1.name)
print(stu1.age)
stu1.eat()
Student.eat(stu1)