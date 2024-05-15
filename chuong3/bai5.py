class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo 
        self.soMu = soMu
        self.keTiep = None 
        
class DaThuc:
    def __init__(self):
        self.head = None
    
    def them(self, heSoMoi, soMuMoi):
        so_da_thuc = Node(heSoMoi, soMuMoi)
        if self.head is None: # Nếu đa thức rỗng 
            self.head = so_da_thuc # phần đầu danh sách chỉ vào nút mới
            
        else: 
            cuoi = self.head
            while cuoi.keTiep: # kiễm tra nút kế tiếp của nút cuối bằng none không
                if cuoi.keTiep.soMu < so_da_thuc.soMu:  #nếu node kế tiếp có số mũ < số mũ node cần được thêm
                    cuoi.keTiep, so_da_thuc.keTiep = so_da_thuc, cuoi.keTiep 
                    return
                cuoi = cuoi.keTiep # duyệt qua từng phần tử của list
            if cuoi.soMu < so_da_thuc.soMu: # cũng giống như trên nhưng dành cho node đầu tiên 
                self.head, so_da_thuc.keTiep = so_da_thuc, cuoi
            else:
                cuoi.keTiep = so_da_thuc
            
    def rutGon(self): # thay thế các số mũ cùng nhau hoặc tổng các số mũ cùng nhau hoặc loại bỏ số mũ 0
        goc = self.head
        truoc_goc = goc # nút truoc_goc là nút gốc trước đó
        while goc:
            timkiem = goc.keTiep
            while timkiem: 
                if timkiem.soMu == goc.soMu: # Nếu tìm thấy một nút với số mũ giống nhau
                    goc.heSo += timkiem.heSo # cộng hệ số của nút đó vào hệ số của nút gốc
                    goc.keTiep = timkiem.keTiep #  loại bỏ nút đó ra khỏi danh sách
                timkiem = timkiem.keTiep
                
            if goc.heSo == 0: # kiểm tra xem hệ số của nút goc có bằng 0 không. Nếu có loại bỏ nút đó khỏi danh sách
                if goc.keTiep is None: # Nếu goc.keTiep is None,tức là goc là nút cuối cùng của danh sách, 
                    truoc_goc.keTiep = None  # nó sẽ chỉnh sửa tham chiếu từ nút trước đó (truoc_goc) để trỏ tới None, loại bỏ nút goc ra khỏi danh sách.
                    
                elif goc == self.head: # Nếu goc == self.head, tức là goc là nút đầu tiên của danh sách, 
                    self.head = goc.keTiep  # nó sẽ chỉnh sửa self.head để trỏ tới nút kế tiếp của goc (goc.keTiep), và sau đó di chuyển tham chiếu truoc_goc tới self.head.
                    truoc_goc = self.head   
            
                else:
                    truoc_goc.keTiep = goc.keTiep
                goc = truoc_goc
            else:
                goc = goc.keTiep # để xử lý các nút tiếp theo trong danh sách.
                               
    def inDaThuc(self):
        temp = self.head
        while temp:
            if temp.heSo > 0:  # Nếu hệ số là số dương,  in dấu cộng; 
                dau = '+'
            elif temp.heSo < 0: # nếu là số âm, in dấu trừ. 
                dau = '-'
            else:
                dau = ' ' # nếu hệ số là 0, bỏ qua in dấu

            if (temp.heSo == -1 or temp.heSo == 1) and temp.soMu > 0 : # nếu hệ số là 1 hoặc -1, bỏ qua in hệ số đó
                so = ''
            else:
                so = abs(temp.heSo)
            
            
            # ghép các chuỗi thành một đa thức hoàn chỉnh và in ra
            if temp.soMu == 0:
                DaThuc = ['' if temp == self.head and temp.heSo > 0 else dau , so]
            elif temp.soMu == 1:
                DaThuc = ['' if temp == self.head and temp.heSo > 0 else dau, '' if so is None else so,'x']
            else:
                DaThuc = ['' if temp == self.head and temp.heSo > 0 else dau,'' if so is None else so,'x^' if temp.soMu > 0 else '', temp.soMu if temp.soMu else '']
            
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            temp = temp.keTiep
        print()
        
    def tich(self, daThuc2):
        traVe = DaThuc() # Tạo một đối tượng mới là traVe để lưu trữ kết quả phép nhân.
        lapPhanTu1 = self.head 
        
        while lapPhanTu1 is not None: # Sử dụng con trỏ lapPhanTu1 để duyệt qua danh sách liên kết của đa thức thứ nhất.
            lapPhanTu2 = daThuc2.head
            while lapPhanTu2 is not None:
                heSo = lapPhanTu1.heSo * lapPhanTu2.heSo
                soMu = lapPhanTu1.soMu + lapPhanTu2.soMu
                traVe.them(heSo, soMu)
                lapPhanTu2 = lapPhanTu2.keTiep
            lapPhanTu1 = lapPhanTu1.keTiep

        traVe.rutGon()
        return traVe

# Tạo đa thức 1
dathuc1 = DaThuc()
dathuc1.them(3, 3)
dathuc1.them(-4, 2)
dathuc1.them(1, 1)
dathuc1.them(6, 0)
dathuc1.inDaThuc()

# Tạo đa thức 2
daThuc2 = DaThuc()
daThuc2.them(2, 2)
daThuc2.them(-3, 1)
daThuc2.them(2, 0)
daThuc2.inDaThuc()

# Tính tích của đa thức 1 và đa thức 2
tich_daThuc = dathuc1.tich(daThuc2)

# In đa thức kết quả
tich_daThuc.inDaThuc()