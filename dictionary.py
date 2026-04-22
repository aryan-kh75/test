dict={
    "name":"John",
    "age":23,
    "height":175.5,
    "married":False,
    "city":"New York"
}
print(dict) 

#to access a value in the dictionary we can use the key
print(dict["name"]) 
print(dict["age"])
print(dict["height"])
print(dict["married"])
print(dict["city"])

#to add a new key-value pair in the dictionary we can use the assignment operator
dict["country"]="USA"
print(dict)

#to pop a key-value pair from the dictionary we can use pop() method
dict.pop("married")
print(dict)

#to update a value in the dictionary we can use the key and assign a new value
dict["age"]=24
print(dict) 