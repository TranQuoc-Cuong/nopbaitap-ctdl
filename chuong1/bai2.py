def giaiThua(n): #Tính giai thừa
    if n == 0:
        return 1
    else:
        return n * giaiThua(n -1)
    
def neper(n):
    tong = 0
    for k in range(n + 1): #tinh tổng một phần giai thừa k
        tong += 1 / giaiThua(k)
    return tong

n = int(input("Nhap vao n: "))

print(f"Neper({n}) = {neper(n)}")