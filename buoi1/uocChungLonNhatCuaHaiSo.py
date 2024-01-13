def uocChungLonNhatCuaHaiSo(so_1, so_2):
    if so_1 >= so_2:
        if so_2 == 0:
            return so_1
        else:
            return uocChungLonNhatCuaHaiSo(so_2, int(so_1 % so_2))
    else:
        if so_1 == 0:
            return so_2
        else:
            return uocChungLonNhatCuaHaiSo(so_1, int(so_2 % so_1))
        
so_1 = int(input("Nhap so thu nhat: "))
so_2 = int(input("Nhap so thu hai: "))
print(uocChungLonNhatCuaHaiSo(so_1, so_2))
