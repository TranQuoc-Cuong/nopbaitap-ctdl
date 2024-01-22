from array import*
mang = array('i', [])

mang = [[1,2,3],[4,5,6],[7,8,9]]

temp = mang[0][0]
mang[0][0] = mang[2][0]
mang[2][0] = mang[2][2]
mang[2][2] = mang[0][2]
mang[0][2] = temp

temp = mang[0][1]
mang[0][1] = mang[1][0]
mang[1][0] = mang[2][1]
mang[2][1] = mang[1][2]
mang[1][2] = temp

for i in mang:
    print(i)

