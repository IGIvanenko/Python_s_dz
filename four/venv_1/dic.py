def flatten_dict(d):
    return [x for y in d.items() for x in y]

print(flatten_dict)