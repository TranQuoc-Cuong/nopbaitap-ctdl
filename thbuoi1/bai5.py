def tonguocso(x):
    s = 0
    for i in range(1, x):
        if x % i == 0:
            s += i
    return s

def phanloai(x):
    s = ""
    tonguoccuaso = tonguocso(x)
    if tonguoccuaso < x:
        s = "deficient"

    elif tonguoccuaso == x:
        s = "perfect"

    else:
        s = "abundant"

    return s

def phanloaimotloat(x, y):
    for i in range (x, y+1):
        print(i, "la", phanloai(i))
    
x = int(input("nhap x:"))
y = int(input("nhap y:"))
phanloaimotloat(x,y)