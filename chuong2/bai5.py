class Mang:
    def __init__(self, mang):
        self.mang = mang
        
    def Cong(self,b):
        a = self.mang
        soA = int(''.join(map(str, a))) # Chuyển đổi mảng thành số nguyên
        soB = int(''.join(map(str, b))) # Chuyển đổi mảng thành số nguyên

        ketqua = soA + soB # Tính tổng

        if ketqua > 2 ** 31 - 1:  # Kiểm tra tràn số
            return [-1] # Nếu kết quả vượt qua giới hạn của số nguyên 32-bit (2^31 - 1), trả về [-1] để chỉ ra rằng đã xảy ra tràn số.

        return ketqua # Phương thức trả về một số nguyên là kết quả của a + b nếu kết quả không bị tràn
    
    
a = Mang([1, 2, 3])

b = [4, 5, 6]
print(a.Cong(b))

b = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(a.Cong(b))