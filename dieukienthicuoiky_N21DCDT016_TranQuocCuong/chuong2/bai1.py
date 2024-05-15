class Mang:
    def __init__(self, mang):
        self.mang = mang
        
    def DoiXung(self):

        kichthuoc = len(self.mang)
        
        for i in range(kichthuoc):
            for j in range(i + 1, kichthuoc):
                if self.mang[i][j] != self.mang[j][i]:
                    return False
        return True

# Ma trận vuông đối xứng
mang = Mang([[1, 2, 3],
             [2, 4, 5],
             [3, 5, 6]])

print(mang.DoiXung())  

# Ma trận vuông không đối xứng
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

print(mang.DoiXung()) 