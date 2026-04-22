num = 20
print(type(num))

num=2.0
print(type(num))

num={'key':20}
print(type(num))

num={1,2,3,4,5}
print(type(num))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
    def __repr__(self):
        return f"Person(name='{self.name!r}', age={self.age!r})"
    
P1 = Person("Alice and wonderland", 30)
P2 = Person("Bob", 25)

print(P1)                #Person(name='Alice', age=30)
print(P1.greet())       #Hello, my name is Alice and I am 30 years old.
print(P2.name,P2.age)   #Bob 25