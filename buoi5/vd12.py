newTuple = ('a', 'b', 'c', 'd', 'e')

def seachTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} is found at {i} index"
    return "the element is not found"

print(seachTuple(newTuple, 'b'))