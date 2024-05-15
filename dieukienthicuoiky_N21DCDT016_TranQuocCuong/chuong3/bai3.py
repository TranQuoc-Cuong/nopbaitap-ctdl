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

    def cong(self, daThuc2):
        traVe = DaThuc() # tạo một đối tượng mới là traVe để lưu trữ kết quả phép cộng.
        phanTu1 = self.head
        phanTu2 = daThuc2.head
        
        while phanTu1 is not None and phanTu2 is not None: # Hai con trỏ phanTu1 và phanTu2 được sử dụng để duyệt qua hai danh sách liên kết của các hạng tử của hai đa thức.
            if phanTu1.soMu > phanTu2.soMu: #nếu số mủ phần tử 1 lớn hơn số mủ phần tử 2
                traVe.them(phanTu1.heSo, phanTu1.soMu) # thêm phần tử 1 vào trong traVe
                phanTu1 = phanTu1.keTiep #phẩn tử 1 trỏ vào phần tử kế tiếp
            elif phanTu1.soMu < phanTu2.soMu: #nếu phần tử 2 lớn hơn số mủ phần tử 1
                traVe.them(phanTu2.heSo, phanTu2.soMu) # thêm phần tử 2 vào trong traVe
                phanTu2 = phanTu2.keTiep #phẩn tử 1 trỏ vào phần tử kế tiếp
            else: # nếu bằng nhau thì cộng hai phần tử lại
                heSo_tong = phanTu1.heSo + phanTu2.heSo
                if heSo_tong != 0: # Nếu kết quả khác 0, hạng tử mới sẽ được thêm vào traVe.
                    traVe.them(heSo_tong, phanTu1.soMu) #thêm đã cộng vào trong traVe
                phanTu1 = phanTu1.keTiep #phần tử 1 trỏ về phần tử kế tiếp
                phanTu2 = phanTu2.keTiep #phần tử 2 trỏ về phần tử kế tiếp

        # Sau khi duyệt qua tất cả các hạng tử của cả hai đa thức, các hạng tử còn lại của phanTu1 và phanTu2 sẽ được thêm vào traVe.
        while phanTu1 is not None:
            traVe.them(phanTu1.heSo, phanTu1.soMu)
            phanTu1 = phanTu1.keTiep

        while phanTu2 is not None:
            traVe.them(phanTu2.heSo, phanTu2.soMu)
            phanTu2 = phanTu2.keTiep

        return traVe
    
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


# Tạo đa thức 1
dathuc1 = DaThuc()
dathuc1.them(3, 3)
dathuc1.them(-3, 3)
dathuc1.them(-2, 2)
dathuc1.them(4, 1)
dathuc1.them(5, 0)
dathuc1.rutGon()
dathuc1.inDaThuc()  

# Tạo đa thức 2
dathuc2 = DaThuc()
dathuc2.them(2, 2)
dathuc2.them(-3, 1)
dathuc2.them(2, 0)
dathuc2.rutGon()
dathuc2.inDaThuc()  

# Cộng hai đa thức
dathuc_ketqua = dathuc1.cong(dathuc2)
dathuc_ketqua.rutGon()
dathuc_ketqua.inDaThuc() 