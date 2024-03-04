def reverse_dict(dict):
    my_dictnew = {value:key for key, value in dict.items()}
    print(my_dictnew)

my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)