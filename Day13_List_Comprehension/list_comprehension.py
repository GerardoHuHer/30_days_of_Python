# Syntax
# [i for i in iterable if expression]

# One way
print("Python list with list() method")
language = "Python"
lst = list(language)
print(type(lst))
print(lst)

# Another way with list comprehension
print("Python list with list comprehension")
lst = [i for i in language]
print(type(lst))
print(lst)

print("")
# Generating numbers 
print("List of numbers generated with list comprehension")
print("[i for i in range(11)]")
numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration
print("List of square numbers generated with list comprehension")
print("[i * i for i in range(11)]")
squares = [i * i for i in range(11)]
print(squares)

# It also possible to make a list of tuples 
print("List of numbers and square numbers in a tuple generated with list comprehension")
print("[(i, i * i) for i in range(11)]")
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Generating even numbers 
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers 
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# even and positive numbers
numbers = [-8, -7, -6, -5, -1, 2, 5, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)

# Flattening a three dimensional arrays
list_of_lists = [[1,2,3], 
                [4,5,6], 
                [7,8,9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)

