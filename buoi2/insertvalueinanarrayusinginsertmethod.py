from array import*

mang = array('i', [2,4,5,3,9])

for i in mang:
    print(i, end=' ')

print()

vi_tri = int(input("Nhap vi tri can chen:"))
gia_tri_can_chen = int(input("Gia tri can chen:"))

mang.insert(vi_tri, gia_tri_can_chen)

for i in mang:
    print(i, end=' ')