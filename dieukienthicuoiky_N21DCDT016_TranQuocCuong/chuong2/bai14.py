class Mang:
    def __init__(self, mang):
        self.mang = mang   
        
    def DayConDauTien(self, b):
        c = [] 
        a = self.mang
        i = 0
        while i < len(a): # nếu a[i] cũng có trong mảng b, chúng ta bắt đầu kiểm tra dãy con từ vị trí hiện tại trong mang.
            if a[i] in b:
                c.append(a[i])

                # Kiểm tra dãy con từ vị trí hiện tại trong a
                j = b.index(a[i]) + 1 # trả về vị trí của giá trị a[i] trong mảng b
                k = i + 1
                
                # Nếu tìm thấy một dãy con giống với b, trả về dãy con đó
                while j < len(b) and k < len(a) and a[k] == b[j]:
                    c.append(a[k])
                    j += 1
                    k += 1

                if len(c) > 0:
                    return c

                c = []  # Reset mảng c nếu không tìm thấy dãy con
            i += 1
        return c
    
a = Mang([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = [9, 8, 7, 3, 4, 6, 5]
print(a.DayConDauTien(b))