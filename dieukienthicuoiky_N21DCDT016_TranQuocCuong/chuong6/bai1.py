def bubbleSort(danhSach):
    for i in range(len(danhSach) - 1):
        for j in range(len(danhSach) - i - 1):
            if danhSach[j] > danhSach[j + 1]:
                danhSach[j], danhSach[j + 1] = danhSach[j + 1], danhSach[j]
    return danhSach

class PhuongThuc:
    def __init__ (self, mang):
        self.mang = mang  # Gán mảng đầu vào cho thuộc tính mang của lớp

    def duyNhat(self):
        numbers = list(set(self.mang)) # Lấy danh sách các số duy nhất từ mảng mang bằng cách sử dụng set (loại bỏ các phần tử trùng lặp)
        # Trả về danh sách các số duy nhất đã được sắp xếp
        return bubbleSort(numbers)

a = PhuongThuc([1, 5, 3, 7, 5, 9, 7])

print(a.mang)

b = a.duyNhat()

print(b)