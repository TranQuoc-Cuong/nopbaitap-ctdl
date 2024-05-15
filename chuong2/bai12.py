class Mang:
    def __init__(self, mang, dau):
        self.mang = mang  
        self.dau = dau 
        
    def layDau(self):
        return 1 if self.dau == 0 else -1 
        
    def Tru(self, b):
        so_a = int(''.join(map(str, self.mang)))
        so_b = int(''.join(map(str, b.mang)))
        
        result = self.layDau()*so_a - so_b*b.layDau()

        if result > 2 ** 31 - 1 or result < -2 ** 31 - 1:
            return [-1]

        return result
    
a = Mang([4, 3, 2], 0) 
b = Mang([1, 2, 3], 1) 
print(a.Tru(b)) 

b = Mang([3, 1, 4, 7, 4, 8, 3, 6, 4, 8],0)
print(a.Tru(b))