#checking whether there is atleast one common item in different list
def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([10,20,46,15,20], [170,14,8,9,14]))
print(common_data([14,110,20,15,2], [15,170,110,37,19]))

