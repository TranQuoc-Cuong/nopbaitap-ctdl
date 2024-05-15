class Mang:
    def __init__(self, mang):
        self.mang = mang  
        
    def DayConDaiNhat(self, b):
        c = []  # Mảng chứa dãy con có chiều dài lớn nhất
        a = self.mang
        for i in range(len(a)):
            for j in range(len(b)): # lặp qua từng phần tử i trong mảng mang và từng phần tử j trong mảng b.
                
                if a[i] == b[j]: # Nếu a[i] =  b[j], bắt đầu kiểm tra dãy con từ vị trí hiện tại trong mang.
                    xoay_c = [a[i]]
                    k = 1

                    while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                        # điều kiện i + k < len(a) và j + k < len(b) tức là không vượt qua phạm vi của mảng
                        #  so sánh các phần tử a[i + k] và b[j + k]
                        xoay_c.append(a[i + k]) #  mở rộng dãy xoay_c bằng cách thêm phần tử a[i + k]
                        k += 1

                    if len(xoay_c) > len(c): # so sánh chiều dài của dãy xoay_c này với dãy có length nhất (c). 
                        c = xoay_c # Nếu dãy mới dài hơn, chúng ta cập nhật c bằng dãy mới này.
        return c
    
a = Mang([1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5])
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
print(a.DayConDaiNhat(b))