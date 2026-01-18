class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old!")

p1=Person("Bruno",24)
print(p1.info())
        