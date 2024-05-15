class Mang:
    def __init__(self, mang, dau):
        self.mang = mang   
        self.dau = dau 
        
    def layDau(self):
        return 1 if self.dau == 0 else -1 # Trả về 1 nếu dau là 0 (dương) và trả về -1 nếu dau là 1 (âm).
        
    def Cong(self, b): 
        so_a = int(''.join(map(str, self.mang))) 
        so_b = int(''.join(map(str, b.mang)))
        
        tong = self.layDau()*so_a + so_b*b.layDau() # tổng của hai số nguyên này được tính toán, với việc áp dụng dấu của từng số bằng cách sử dụng phương thức layDau().
        
        if tong > 2 ** 31 - 1 or tong < -2 ** 31 - 1:  # Kiểm tra tràn số
            return [-1]

        return tong
    
a = Mang([1, 2, 3], 0)  
b = Mang([4, 5, 6], 1) 
print(a.Cong(b))


b = Mang([2, 1, 4, 7, 4, 8, 3, 6, 4, 8],  0)
print(a.Cong(b)) 