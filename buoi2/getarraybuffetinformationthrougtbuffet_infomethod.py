from array import array

mang = array('i', [1,2,3,4])

for i in mang:
    print(i, end=' ')

print()

print(mang.buffer_info())