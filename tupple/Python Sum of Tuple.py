#Using list() + sum() to Find Python Sum of Tuple
def summation(test_tup):
    test = list(test_tup)
    count = 0
    for i in test:
        count += i
    return count
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))
