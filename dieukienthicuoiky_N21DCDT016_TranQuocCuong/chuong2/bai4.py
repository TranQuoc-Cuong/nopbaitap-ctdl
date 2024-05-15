class Mang:
    def __init__(self, mang):
        self.mang = mang
        
    def NhomHang(self):
        kichthuoc = len(self.mang)
        
        nhom_hang = {}

        for i in range(kichthuoc):
            hang = str(self.mang[i])

            if hang in nhom_hang: # Nếu hàng đã tồn tại trong từ điển, thêm chỉ mục hàng vào nhóm tương ứng
                nhom_hang[hang].append(i)
            else:
                
                nhom_hang[hang] = [i] # Nếu hàng chưa tồn tại, tạo một nhóm mới với chỉ mục hàng hiện tại
     
        for nhom in nhom_hang.values():
            print("Nhóm chỉ mục hàng:", nhom)

# Ma trận với các hàng giống nhau
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [1, 2, 3]])

mang.NhomHang()

print()

# Ma trận với các hàng không giống nhau
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
mang.NhomHang() 