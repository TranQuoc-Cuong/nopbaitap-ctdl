class Mang:
    def __init__(self, mang):
        self.mang = mang
        
    def TamGiacTren(self):

        kichthuoc = len(self.mang)

        for i in range(kichthuoc):
            for j in range(i):
                if self.mang[i][j] != 0: # kiểm tra từng phần tử của ma trận để xem xét nếu có bất kỳ phần tử nào nằm dưới đường chéo chính khác 0.
                    return False
        return True
    
 # Ma trận tam giác trên    
mang = Mang([[1, 2, 3],
             [0, 4, 5],
             [0, 0, 6]])

print(mang.TamGiacTren())  

# Ma trận không phải tam giác trên
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

print(mang.TamGiacTren()) 