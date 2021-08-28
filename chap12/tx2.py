class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu1=Student('张三',30)
stu1.show()
print(stu1.name)
print(stu1._Student__age)  #强行读取