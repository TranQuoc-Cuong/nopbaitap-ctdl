def gcd_de_quy(m, n): #tim ước chung bằng đề quy
    if n == 0:
        return m
    else:
        return gcd_de_quy(n, m % n)

def gcd_vong_lap(m, n):  #tim ước chung bằng vòng lặp
    while n != 0:
        n, m = m % n, n
    return m

n = int(input("Nhap vao n: ")) 
m = int(input("Nhap vao m: "))

print("GCD su dung de quy:", gcd_de_quy(n, m))
print("GCD su dung vong lap:", gcd_vong_lap(n, m))