#wight = 10
#sorted_things = dict(sorted(things.items(), key=lambda x: -x[1]))
#for k, w in sorted_things.items():
#	if w <=  wight:
#         print(k, sep='/n')
#         wight -= w
#
#things = {'палатка': 3, 'спальник': 1, 'вода': 2, 'аптечка': 1, 'продукты': 2, 'одежда': 2, 'посуда': 2, 'лодка': 5}


def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'палатка': 3, 'спальник': 1, 'вода': 2, 'аптечка': 1, 'продукты': 2, 'одежда': 2, 'посуда': 2, 'лодка': 5}
max_weight = 10
print(pack_backpack(items, max_weight))