unsorted_list = [1, 3, 7, 10, 54, 100]
range_list = range(unsorted_list[0], unsorted_list[-1])
print(range_list)
new_list = []
for x in range_list:
    print(x)
    if x not in unsorted_list:
        new_list.append(x)
print(new_list)
