class mang:
    def __init__(self):
        self.matran = []
        self.soluongphantu = 0
    
    def NhapSoLuongPhanTu(self):
        self.soluongphantu = int(input("Nhap so luong phan tu cua ma tran vuong: "))
    
    def NhapPhanTu(self):
        print("Nhập các phần tử của ma trận:")
        for i in range(self.soluongphantu):
            self.matran.append([])
            for j in range(self.soluongphantu):
                phan_tu = int(input(f"Nhập phần tử [{i}][{j}]: "))
                self.matran[i].append(phan_tu)
    
    def InPhanTu(self):
        print("Các phần tử của ma trận:")
        for i in range(self.soluongphantu):
            for j in range(self.soluongphantu):
                print(self.matran[i][j], end=" ")
            print()
    
    def DoiXung(self):
        for i in range(self.soluongphantu):
            for j in range(self.soluongphantu):
                if self.matran[i][j] != self.matran[j][i]:
                    return False
        return True
    
    def TamGiacTren(self):
        for i in range(self.soluongphantu):
            for j in range(i):
                if self.matran[i][j] != 0:
                    return False
                return True
    
    def TrungHang(self):
        temp = 0
        for i in range(self.soluongphantu):
            for j in range(i + 1, self.soluongphantu):
                for k in range(self.soluongphantu):
                    if self.matran[i][k] == self.matran[j][k]:
                        temp += 1
                if temp == self.soluongphantu:
                    return True
                temp = 0
        return False
    

    
m = mang()
m.NhapSoLuongPhanTu()   
m.NhapPhanTu()
m.InPhanTu()

print(m.DoiXung())

print(m.TamGiacTren())

print(m.TrungHang())

