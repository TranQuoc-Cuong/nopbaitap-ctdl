from array import*

mang = array('i', [2,6,4,7])

n = int(input("nhap so luong phan tu nhap vao cuoi mang: "))

print("mang ban dau:", mang)

for i in range(n):
    temp = int(input())
    mang.append(temp)

print("mang sau khi nhap:", mang)