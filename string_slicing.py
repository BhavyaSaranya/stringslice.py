
name = "bhavyasaranya"
print(name[0:4])
print(name[1:5])
print(name[ : ])
print(name[1:])

#reverse a string

name = "bhavya"
str = (name[::-1])
print(str)

# reverse a string without slicing

name = "bhavya"
str = "".join(reversed(name))
print(str)

# reverse a list items

names = list(("malika","bhavya","priyam"))
print(names[::-1])