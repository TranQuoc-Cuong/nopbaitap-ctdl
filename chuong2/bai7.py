class Mang:
    def __init__(self, mang):
        self.mang = mang # Khởi tạo một đối tượng Mang với một thuộc tính là một mảng mang.
        
    def Nhan(self,b):
        a = self.mang
        soA = int(''.join(map(str, a)))
        soB = int(''.join(map(str, b)))

        ketqua = soA * soB

        if ketqua > 2**31 - 1:
            return [-1]
        return ketqua
    
a = Mang([1, 2, 3])

b = [4, 5, 6]
print(a.Nhan(b))


b = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(a.Nhan(b))