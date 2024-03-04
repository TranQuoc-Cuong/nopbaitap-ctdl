def max_value_key(my_dict):
    print(max(my_dict, key =my_dict.get))

my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)