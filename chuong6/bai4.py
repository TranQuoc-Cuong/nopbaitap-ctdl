def bubbleSort(danhSach):
    for i in range(len(danhSach) - 1):
        for j in range(len(danhSach) - i - 1):
            if danhSach[j] > danhSach[j + 1]:
                danhSach[j], danhSach[j + 1] = danhSach[j + 1], danhSach[j]
    return danhSach

class PhuongThuc:
    def __init__ (self, mang):
        self.mang = mang
        
    def Hop(self, b):
        set_a = set(self.mang)  # Tạo tập hợp từ mảng a
        set_b = set(b)  # Tạo tập hợp từ mảng b
        tamthoi = set_a | set_b  # Lấy hợp của hai tập hợp
        sorted_tamthoi = bubbleSort(list(tamthoi))  # Sắp xếp kết quả theo thứ tự tăng dần
        return sorted_tamthoi

a = PhuongThuc([1, 5, 3, 7, 9, 4, 2])
b = [9, 6, 2, 3, 8]
c = a.Hop(b)
print(c)