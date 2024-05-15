def bubbleSort(danhSach):
    for i in range(len(danhSach) - 1):
        for j in range(len(danhSach) - i - 1):
            if danhSach[j] > danhSach[j + 1]:
                danhSach[j], danhSach[j + 1] = danhSach[j + 1], danhSach[j]
    return danhSach

class PhuongThuc:
    def __init__ (self, mang):
        self.mang = mang
        
    def Hieu(self, b):
        set_a = set(self.mang)  # Tạo tập hợp từ mảng a
        set_b = set(b)  # Tạo tập hợp từ mảng b
        khacbiet = set_a - set_b  # Lấy hiệu của hai tập hợp
        sorted_khacbiet = bubbleSort(list(khacbiet))  # Sắp xếp kết quả theo thứ tự tăng dần
        return sorted_khacbiet

a = PhuongThuc([1, 5, 3, 7, 9, 4, 2])
b = [9, 6, 2, 3, 8]
c = a.Hieu(b)
print(c)