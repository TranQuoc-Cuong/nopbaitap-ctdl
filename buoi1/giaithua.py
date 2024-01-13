def giaiThua(x):
    assert x >= 0 and int(x) == x
    if x in [0,1]:
        return 1
    else:
        return x * giaiThua(x - 1)
    
n = int(input("nhap n: "))
print(giaiThua(n))
