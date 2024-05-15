class Mang:
    def __init__(self, mang):
        self.mang = mang # Khởi tạo một đối tượng Mang với một thuộc tính là một mảng mang.
        
    def Tru(self,b):
        a = self.mang
        soA = int(''.join(map(str, a))) # Chuyển đổi mảng thành số nguyên
        soB = int(''.join(map(str, b))) # Chuyển đổi mảng thành số nguyên

        ketqua = soA - soB
        
        
        if ketqua < -2 ** 31 - 1: # Kiểm tra tràn số
            return [-1]
        return ketqua
    
    
a = Mang([1, 2, 3])

b = [1, 0, 0]
print(a.Tru(b))

b = [3, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(a.Tru(b))