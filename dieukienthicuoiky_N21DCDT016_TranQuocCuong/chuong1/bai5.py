def tong_uoc_so(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def phan_loai_so(n):
    s = tong_uoc_so(n)
    if s < n:
        return 'deficient'
    elif s == n:
        return 'perfect'
    else:
        return 'abundant'
    
def Number(x, y):
    for i in range(x, y + 1):
        phan_loai = phan_loai_so(i)
        print(f"Số {i} là {phan_loai}")

x = int(input("nhap x: "))
y = int(input("Nhap y: "))

Number(x, y)