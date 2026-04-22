#Encapsulation is the process of wrapping data and methods together in a single unit (i.e., class)
#privacy

class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #private variable

p1=person("aryan",20)
print(p1.name,p1._person__age)