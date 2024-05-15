class Mang:
    def __init__(self, mang):
        self.mang = mang  
        
    def TrungCot(self):
        kichthuoc = len(self.mang)

        for i in range(kichthuoc):
            for j in range(i + 1, kichthuoc):   
                cot_i = [self.mang[k][i] for k in range(kichthuoc)] # đưa các phần tử cột thứ i vào trong mang cot_i
                cot_j = [self.mang[k][j] for k in range(kichthuoc)] # đưa các phần tử cột thứ j vào trong mang cot_j
                if cot_i == cot_j: 
                    return True

        return False

# mảng có hai cột giống nhau
mang = Mang([[1, 2, 1],
             [4, 5, 4],
             [7, 8, 7]])
print(mang.TrungCot()) 
    
# mảng không có hai cột giống nhau    
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])

print(mang.TrungCot())