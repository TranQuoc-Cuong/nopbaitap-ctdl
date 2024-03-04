my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

filtered_dict = filtered_dict(my_dict, lambda k, v: v % 2 == 0)
