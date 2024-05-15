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
        tamThoi = self.head
        while tamThoi:
            if tamThoi.heSo > 0:  # Nếu hệ số là số dương,  in dấu cộng; 
                dau = '+'
            elif tamThoi.heSo < 0: # nếu là số âm, in dấu trừ. 
                dau = '-'
            else:
                dau = ' ' # nếu hệ số là 0, bỏ qua in dấu

            if (tamThoi.heSo == -1 or tamThoi.heSo == 1) and tamThoi.soMu > 0 : # nếu hệ số là 1 hoặc -1, bỏ qua in hệ số đó
                so = ''
            else:
                so = abs(tamThoi.heSo)
            
            
            # ghép các chuỗi thành một đa thức hoàn chỉnh và in ra
            if tamThoi.soMu == 0:
                DaThuc = ['' if tamThoi == self.head and tamThoi.heSo > 0 else dau , so]
            elif tamThoi.soMu == 1:
                DaThuc = ['' if tamThoi == self.head and tamThoi.heSo > 0 else dau, '' if so is None else so,'x']
            else:
                DaThuc = ['' if tamThoi == self.head and tamThoi.heSo > 0 else dau,'' if so is None else so,'x^' if tamThoi.soMu > 0 else '', tamThoi.soMu if tamThoi.soMu else '']
            
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            tamThoi = tamThoi.keTiep
        print()

dathuc = DaThuc()
dathuc.them(-4,2)
dathuc.them(5,2)
dathuc.them(-6,2)
dathuc.them(3,1)
dathuc.them(-4,1)
dathuc.them(-5,0)
dathuc.inDaThuc() 
dathuc.rutGon()
dathuc.inDaThuc() 