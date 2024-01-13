def luyThuaCuaMotSo(so_a, bac_cua_so_a):
    if bac_cua_so_a == 0:
        return 1
    else:
        return so_a * luyThuaCuaMotSo(so_a, bac_cua_so_a - 1)
    

so_a = int(input("nhap so a: "))
bac_cua_so_a = int(input("nhap bac cua so a: "))
print(luyThuaCuaMotSo(so_a, bac_cua_so_a))