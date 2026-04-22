#creating a list
my_list=[1,2,3,4,5]

print(*my_list)
#to access an element in the list we can use index
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])

#to replace an element in the list we can use index and assign a new value
my_list[3]=10
print(my_list)

#to insert a new element in the list we can use append() and insert() method
my_list.append(6)
print(my_list)

#to insert a new element at a specific position we can use insert() method
my_list.insert(1,9)
print(my_list)

#to remove an element from the list we can use remove() method
my_list.remove(3)
print(my_list)

#to remove an element at a specific position we can use pop() method (index value)
my_list.pop(2)
print(my_list)