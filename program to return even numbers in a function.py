# function program to return even numbers in a list to a new list
def my_numbers(numbers): 
    even_numbers = [x for x in numbers if x % 2 == 0]
    return even_numbers

my_list=[1, 122, 67, 79, 4, 278, 7, 14,]
output=my_numbers(my_list)
print(output)


