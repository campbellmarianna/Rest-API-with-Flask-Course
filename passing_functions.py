def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# print(methodception(add_two_numbers))

# print(methodception(lambda: 35 + 77))  # a lambda function is an anonymous function - always one line

my_list = [13, 56, 77, 484]

def not_thirteen(x):
    return x != 13
    
# filter this list using this function - basicly all of the numbers that were not 13
print(list(filter(not_thirteen, my_list))) # method that allows you keep only some values, takes in an iterator

print([x for x in my_list if x != 13])
