class Mang:
    def __init__(self, mang):
        self.mang = mang

    def TrungHang(self):

        kichthuoc = len(self.mang)

        for i in range(kichthuoc):
            for j in range(i + 1, kichthuoc):
                if self.mang[i] == self.mang[j]: # kiểm tra xem có hai hàng nào trong ma trận có giá trị bằng nhau không
                    return True
        return False
    
# Ma trận có hai hàng giống nhau
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [1, 2, 3]])

print(mang.TrungHang())  

# Ma trận không có hai hàng giống nhau
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
print(mang.TrungHang()) 