def merge_dicts(dict1, dict2):
    dictsum = dict1.copy()
    dictsum.update(dict2)
    for key in dict2:
        if key in dict1:
            dictsum[key] = dict2[key] + dict1[key]
    print(dictsum)
    

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
    