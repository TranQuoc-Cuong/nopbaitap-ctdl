class bieuThuc:
    def __init__(self, bieuThuc):
        self.bieuThuc = bieuThuc
    
    def hauToc(self):
        toan_hang_stack = [] # Stack lưu trữ các toán hạng (số)
        toan_tu_stack = []  # Stack lưu trữ các toán tử (+ - * /)
        muc_do_uu_tien = {'+':1, '-':1, '*':2, '/':2 } # Độ ưu tiên của các toán tử
        
        # Tách biểu thức thành các donVi sử dụng split()
        donVis = self.bieuThuc.split() 
        
        for donVi in donVis:
            if donVi.isdigit(): # Nếu donVi là số, đưa vào stack toán hạng
                toan_hang_stack.append(donVi)
            else: # Nếu donVi là toán tử
                # Sử dụng get với từ điển muc_do_uu_tien để tránh lỗi khi gặp các ký tự không phải là toán tử.
                while (toan_tu_stack and muc_do_uu_tien.get(donVi,0) <= muc_do_uu_tien.get(toan_tu_stack[-1],0)):
                    toan_hang_stack.append(toan_tu_stack.pop())
                toan_tu_stack.append(donVi)
                
        while toan_tu_stack: # Đưa các toán tử còn lại vào stack toán hạng
            toan_hang_stack.append(toan_tu_stack.pop())
        return ' '.join(toan_hang_stack) # Trả về chuỗi biểu thức hậu tố


# Tạo một biểu thức số học
bt = bieuThuc('2 * 3 + 5 / 5')

# Chuyển đổi sang dạng hậu tố
bt_hau_to = bt.hauToc() # 2 3 * 5 5 / +

print(bt_hau_to)