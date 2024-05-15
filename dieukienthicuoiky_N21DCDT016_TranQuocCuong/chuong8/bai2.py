class PhuongThuc:
    def __init__(self):
        # Bảng băm có 26 ô cho các ký tự từ 'a' đến 'z'
        self.table = {chr(i):{} for i in range(ord('a'), ord('z')+1)}
        
    def __hash_func(self, word):
        # Hàm băm lấy ký tự đầu tiên
        return word[0].lower() # Đảm bảo xử lý chữ hoa chữ thường
    
    def NhapTu(self, tu, tu_dong_nghia = None, tu_trai_nghia = None):
        
        # Tính vị trí trong bảng băm
        hash_key = self.__hash_func(tu)
        # Thêm từ  vào bucket
        bucket = self.table[hash_key]
        if bucket.get("tu",0) == tu:
            if tu_dong_nghia not in bucket['dong_nghia'] and tu_dong_nghia is not None:
                bucket['dong_nghia'].append(tu_dong_nghia)
            if tu_trai_nghia not in bucket['trai_nghia'] and tu_trai_nghia is not None:
                bucket['trai_nghia'].append(tu_trai_nghia)
            
        else:
            # Tạo một từ điển cho từ này
            word_info = {
                'tu' : tu,
                'dong_nghia' : [],
                'trai_nghia' : []
            }
            if tu_dong_nghia not in word_info['dong_nghia'] and tu_dong_nghia is not None:
                word_info['dong_nghia'].append(tu_dong_nghia)
            if tu_trai_nghia not in word_info['trai_nghia'] and tu_trai_nghia is not None:
                word_info['trai_nghia'].append(tu_trai_nghia)
            self.table[hash_key] = word_info
            
    def TraTu(self, tu):
        # Tìm từ trong bảng băm
        hash_key = self.__hash_func(tu)
        bucket = self.table[hash_key]
        dong_nghia_str = ("")
        trai_nghia_str = ("")
        # Nếu từ trong danh sách bucket
        if bucket.get("tu",0) == tu:
            dong_nghia_str = ', '.join(str(x) for x in bucket['dong_nghia'])
            trai_nghia_str = ' '.join(str(x) for x in bucket['trai_nghia'])
            kq_list = ['từ:',tu,", có từ đồng nghĩa là: ", dong_nghia_str, ", có từ trái nghĩa là: ", trai_nghia_str]            
            for m in kq_list:
                print (m, end= ' ')
            print()
        else:
            print ("Không có từ cần tìm kiếm")  # Nếu không tìm thấy từ

# Tạo từ điển
tu_dien = PhuongThuc()

# Nhập các từ với từ đồng nghĩa và trái nghĩa
tu_dien.NhapTu("nhỏ", tu_dong_nghia="bé")
tu_dien.NhapTu("giàu", tu_dong_nghia="phú quý", tu_trai_nghia="nghèo")

tu_dien.NhapTu("nhỏ", tu_dong_nghia="bé")
tu_dien.NhapTu("giàu", tu_dong_nghia="phú quý", tu_trai_nghia="nghèo")

# Tra từ điển
tu_dien.TraTu("nhỏ")
tu_dien.TraTu("giàu")

        