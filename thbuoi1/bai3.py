def GCD_dequy(m, n):
    if n == 0:
        return m
    else:
        return GCD_dequy(n, m % n)

def GCD_khong_dequy(m, n):
    while n != 0:
        temp = m % n  
        m = n        
        n = temp
    return m

m = int(input("nhap m:"))
n = int(input("nhap n:"))

print("ket qua GCD de quy", GCD_dequy(m, n))
print("ket qua GCD khong de quy", GCD_khong_dequy(m, n))