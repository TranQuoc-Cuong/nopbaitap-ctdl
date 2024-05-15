class Mang:
    def __init__(self, mang, dau):
        self.mang = mang
        self.dau = dau
        
    def layDau(self):
        return 1 if self.dau == 0 else -1 
        
    def Nhan(self, b):
        so_a = int(''.join(map(str, self.mang)))
        so_b = int(''.join(map(str, b.mang)))
        
        ketqua = self.layDau()*so_a * so_b*b.layDau()

        if ketqua > 2 ** 31 - 1 or ketqua < -2 ** 31 - 1:
            return [-1]
        
        return ketqua
    
a = Mang([1, 2, 3], 0)  
b = Mang([4, 5, 6], 1) 
print(a.Nhan(b))  

b = Mang([3, 1, 4, 7, 4, 8, 3, 6, 4, 8],0)
print(a.Nhan(b))  