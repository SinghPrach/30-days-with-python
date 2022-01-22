# Return values using comma
def name():
    return "Prachi", "Singh"


# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)

#Using a dictionary
def name():
    n1 = "Prachi"
    n2 = "Singh"

    return {1: n1, 2: n2}


names = name()
print(names)
