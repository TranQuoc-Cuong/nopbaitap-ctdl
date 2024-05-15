class Mang:
    def __init__(self, mang):
        self.mang = mang

    def tamGiacDuoi(self):
        kichthuoc = len(self.mang)

        for i in range(kichthuoc):
            for j in range(i + 1, kichthuoc):
                if self.mang[i][j] != 0:
                    return False
        return True
    
# mảng Tam Giác dưới
mang = Mang([[1, 0, 0],
             [1, 2, 0],
             [1, 2, 3]])
print(mang.tamGiacDuoi())

# mảng không phải tam giác dưới

mang = Mang([[1, 2, 3],
             [1, 2, 3],
             [1, 2, 3]])
print(mang.tamGiacDuoi())