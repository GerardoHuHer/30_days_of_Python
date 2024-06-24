# syntax
# x = lambda param1, param2, param3: param1 + param2 + param3
# print(x(arg1, arg2, arg3))

def add_two_nums(a, b):
    return a + b

print(add_two_nums(2,3))

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))

# Self invoking lambda function
print((lambda a, b: a + b)(2,3))

#square 
square = lambda x : x ** 2
print(square(3))
cube = lambda x : x ** 3
print(cube(3))

# Multiple variables 
multiple_variables = lambda a, b, c: a ** 2 -3 * b + 4 *c
print(multiple_variables(5,5,3))

# Using lambda functions inside another fuctions 
def power(x: float) -> float:
    return lambda n: x ** n

cube = power(2)(3)
print(cube)

two_power_of_five = power(2)(5)
print(two_power_of_five)


