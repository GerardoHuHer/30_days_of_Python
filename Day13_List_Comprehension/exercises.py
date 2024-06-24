# 1. Filter only negative and zero in the list using list comprehensino
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negatives_and_zero = [i for i in numbers if i <= 0]
print(negatives_and_zero)

# Flatten the following list of lists to a one dimensional list 
list_of_lists = [[[1,2,3]], 
                [[4,5,6]], 
                [[7,8,9]]]
flatten_list = [number for panel in list_of_lists for row in panel for number in row]
print(flatten_list)

# 3 Using list comprehension create the following list of tuples

list_tuple = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(list_tuple)

# 4. Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries_flatten = [ [country[0].upper(), country[0][:3].upper(), country[1].upper()] for list_aux in countries for country in list_aux]
print(countries_flatten)

# 5. Change the following list to a dictionary 
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

dicc = [{"country": country[0], "city": country[1] } for list_aux in countries for country in list_aux]
print(dicc)

# 6. Change the followig list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

list_of_names = [tuple_aux[0] + " " + tuple_aux[1] for list_aux in names for tuple_aux in list_aux]
print(list_of_names)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions

linear_function = lambda x, b : x + b
y = linear_function(5, -4)
print(y)


