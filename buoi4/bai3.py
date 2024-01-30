def doinguoc(x):
    ket_qua = 0

    while x != 0:
        so_cuoi = x % 10
        ket_qua = (ket_qua * 10) + so_cuoi
        x = x // 10

    return ket_qua


a = int(input("nhap vao mot so: "))

print(doinguoc(a))
