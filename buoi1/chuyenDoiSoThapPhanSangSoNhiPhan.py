def chuyenDoiSoThapPhanSangNhiPhan(so_thap_phan):
    if so_thap_phan == 1:
        print(1, end="")
    else:
        chuyenDoiSoThapPhanSangNhiPhan(int(so_thap_phan / 2))
        print(so_thap_phan % 2, end="")
        

so_thap_phan = int(input("nhap so thap phan: "))
chuyenDoiSoThapPhanSangNhiPhan(so_thap_phan)