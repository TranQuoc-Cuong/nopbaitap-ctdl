class Mang:
    def __init__(self, mang):
        self.mang = mang
        
    def NhomCot(self):
        nhom_cot = {}

        kichthuoc = len(self.mang)

        for i in range(kichthuoc):
            for j in range(kichthuoc):
                cot = str(self.mang[j][i]) # Chuyển đổi cột thành chuỗi để sử dụng làm khóa trong từ điển
            if cot in nhom_cot: # Nếu cột đã tồn tại trong từ điển, thêm chỉ mụcvào nhóm tương ứng
                nhom_cot[cot].append(i)
            else:
                nhom_cot[cot] = [i] # Nếu chưa tồn tại, tạo một nhóm mới với chỉ mục hiện tại
         
        for nhom in nhom_cot.values(): # In ra các nhóm chỉ mục hàng
            print("Nhóm chỉ mục cột:", nhom)
            
 
mang = Mang([[1, 2, 1],
             [4, 5, 4],
             [7, 8, 7]])
mang.NhomCot()
print()
    
mang = Mang([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]])
mang.NhomCot()