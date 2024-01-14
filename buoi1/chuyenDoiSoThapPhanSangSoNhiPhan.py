def chuyenDoiSoThapPhanSangNhiPhan(so_thap_phan):
    if so_thap_phan in [0,1]:
        print(so_thap_phan, end="")
    else:
        chuyenDoiSoThapPhanSangNhiPhan(int(so_thap_phan / 2))
        print(so_thap_phan % 2, end="")
        

so_thap_phan = int(input("nhap so thap phan: "))
chuyenDoiSoThapPhanSangNhiPhan(so_thap_phan)