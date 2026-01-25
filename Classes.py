class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old!")

p1=Person("Bruno",24)
print(p1.info())
        

p2=Person("A",45)
print(p2.info())

p3=Person("B",15)
print(p3.info())


class Student(Person):
    def __init__(self,university):
        Person.__init__(self)
        self.university=university
    
    def info(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old! I am studying on the university: {self.university}")