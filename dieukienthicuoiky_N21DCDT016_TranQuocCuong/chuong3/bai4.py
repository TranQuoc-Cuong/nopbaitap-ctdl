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
    
    def doiDau(self):
        lapPhanTu = self.head
        while lapPhanTu is not None:
            lapPhanTu.heSo = -lapPhanTu.heSo
            lapPhanTu = lapPhanTu.keTiep
            
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
                DaThuc = [dau if tamThoi != self.head  else '', so]
            elif tamThoi.soMu == 1:
                DaThuc = [dau if tamThoi != self.head  else '', '' if so is None else so,'x']
            else:
                DaThuc = [dau if tamThoi != self.head  else '','' if so is None else so,'x^' if tamThoi.soMu > 0 else '', tamThoi.soMu if tamThoi.soMu else '']
            
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            tamThoi = tamThoi.keTiep
        print()
        
# Tạo đa thức
dathuc = DaThuc()
dathuc.them(4, 3)
dathuc.them(-5, 2)
dathuc.them(2, 1)
dathuc.them(6, 0)

dathuc.inDaThuc()  


dathuc.doiDau()

dathuc.inDaThuc()  