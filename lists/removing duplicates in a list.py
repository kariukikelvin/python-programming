#program to remove duplicates from a list
list=[5,9,3,6,14,11,9,3,4,11]
duplicate_items = set()
unique_items = []
for y in list:
    if y not in duplicate_items:
        unique_items.append(y)
        duplicate_items.add(y)
print(duplicate_items)
