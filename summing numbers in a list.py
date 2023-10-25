#program to sum of numbers in list
def numbers(num):
    total = 0
    for number in num:
        total += number
    return total


my_list = [67, 18, 109, 277, 9]
result = numbers(my_list)
print("Sum:", result)
