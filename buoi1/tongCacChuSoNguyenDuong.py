def tongCacChuSoNguyenDuong(so_nguyen_duong):
    if (so_nguyen_duong / 10) == 0:
        f = so_nguyen_duong % 10
        return int(f)
    else:
        f = so_nguyen_duong % 10 + tongCacChuSoNguyenDuong(so_nguyen_duong / 10)
        return int(f)
    
so_nguyen_duong = int(input("Nhap so nguyen duong: "))
print(int(tongCacChuSoNguyenDuong(so_nguyen_duong)))