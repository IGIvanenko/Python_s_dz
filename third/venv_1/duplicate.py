my_list = [2, 2, 5, 10, 5, 55, 10, 11, 1]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Список повторяющихся элементов: ", duplicates)



def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicates(lst))
