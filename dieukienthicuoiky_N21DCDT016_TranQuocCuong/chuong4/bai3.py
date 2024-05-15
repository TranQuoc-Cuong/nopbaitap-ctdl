class BieuThuc:
    def __init__(self, bieuThuc):
        self.bieuThuc = bieuThuc
    
    def hauTo(self):
        toan_hang_stack = [] # Stack lưu trữ các toán hạng (số)
        toan_tu_stack = []  # Stack lưu trữ các toán tử (+ - * /)
        muc_do_uu_tien = {'+':1, '-':1, '*':2, '/':2} # Độ ưu tiên của các toán tử
        
        donVis = self.bieuThuc.split()  # Tách biểu thức thành các donVi sử dụng split()
        
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
    
    def giaTri(self):
        bieu_thuc_hau_to = self.hauTo().split()
        tinh_stack= []
        for toan_tu in bieu_thuc_hau_to:
            if toan_tu.isdigit(): # Nếu donVi là số, đưa vào stack tính toán
                tinh_stack.append(float(toan_tu))
            else:
                b = tinh_stack.pop() # Lấy 2 số từ stack
                a = tinh_stack.pop()
                tinh_stack.append(self.apply_operation(toan_tu,a,b)) # Thực hiện phép toán và đưa kết quả lại vào stack
                
        print(tinh_stack.pop()) # In kết quả cuối cùng
                
    def apply_operation(self, operator, a, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b # Sử dụng phép chia thực (float division) để tránh lỗi chia cho 0
        


bt = BieuThuc('2 * 3 / 4 + 8 - 2 + 1 ')

bt.giaTri()# Tính giá trị của biểu thức và in kết quả = 8.5


bt = BieuThuc('2 + 3 * 4')
bt.giaTri()# Tính giá trị của biểu thức và in kết quả = 14