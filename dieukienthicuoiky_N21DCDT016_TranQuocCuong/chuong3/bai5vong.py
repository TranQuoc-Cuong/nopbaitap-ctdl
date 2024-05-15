class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo
        self.soMu = soMu
        self.keTiep = None
        
class DaThuc:
    def __init__(self):
        self.head = None

    def them(self, heSoMoi, soMuMoi): # thêm một hạng tử mới vào đa thức theo thứ tự giảm dần của số mũ.
        nutMoi = Node(heSoMoi,soMuMoi)
        if self.head is None: # Nếu đa thức rỗng 
            self.head = nutMoi # nó sẽ trở thành nút đầu tiên của đa thức
            nutMoi.next = self.head
            
        else: # Nếu không, nó sẽ duyệt qua các nút trong danh sách đến khi tìm được vị trí thích hợp cho nút mới dựa trên số mũ.
            cuoiCung = self.head 
            while cuoiCung.keTiep and (cuoiCung.keTiep != self.head): # kiểm tra node kế tiếp nếu node đó không = none
                if cuoiCung.keTiep.soMu < nutMoi.soMu:  #nếu node kế tiếp có số mũ < số mũ node cần được thêm
                    tamThoi = cuoiCung.keTiep # lưu giá trị kế tiếp của cuoiCung vào tamThoi
                    cuoiCung.keTiep = nutMoi # thay đổi giá trị kế tiếp của cuoiCung thành node mới
                    nutMoi.keTiep = tamThoi # thêm giá trị kế tiếp cho node mới từ tamThoi
                    return
                cuoiCung = cuoiCung.keTiep # duyệt qua từng phần tử của list
                
            if cuoiCung.soMu < nutMoi.soMu: # cũng giống như trên nhưng dành cho node đầu tiên 
                tamThoi = cuoiCung
                self.head = nutMoi
                tamThoi.keTiep = self.head
                nutMoi.keTiep = tamThoi
            else:
                nutMoi.keTiep = self.head
                cuoiCung.keTiep = nutMoi
    
    def rutGon(self):
        goc = self.head
        truocGoc = goc # nút truocGoc là nút goc trước đó 
        while True:
            timKiem = goc.keTiep
            while timKiem != goc: # bắt đầu bằng cách duyệt qua từng nút trong danh sách
                if timKiem.soMu == goc.soMu: # Nếu tìm thấy một nút với số mũ giống nhau
                    goc.heSo += timKiem.heSo # cộng hệ số của nút đó vào hệ số của nút gốc
                    goc.keTiep = timKiem.keTiep #  loại bỏ nút đó ra khỏi danh sách
                timKiem = timKiem.keTiep
                
            # Sau khi duyệt qua tất cả các nút
            if goc.heSo == 0: # kiểm tra xem hệ số của nút goc có bằng 0 không. Nếu có loại bỏ nút đó khỏi danh sách
                # Nếu goc.keTiep is None,tức là goc là nút cuối cùng của danh sách, 
                # nó sẽ chỉnh sửa tham chiếu từ nút trước đó (truocGoc) để trỏ tới None, loại bỏ nút goc ra khỏi danh sách.
                if goc.keTiep == self.head: 
                    truocGoc.keTiep = None 
                    
                # Nếu goc == self.head, tức là goc là nút đầu tiên của danh sách, 
                # nó sẽ chỉnh sửa self.head để trỏ tới nút kế tiếp của goc (goc.keTiep), và sau đó di chuyển tham chiếu truocGoc tới self.head.
                elif goc == self.head:
                    self.head = goc.keTiep
                    truocGoc = self.head   
                
                # Trong trường hợp còn lại, 
                # nó chỉnh sửa tham chiếu của nút trước đó (truocGoc) để trỏ tới nút kế tiếp của goc (goc.keTiep), 
                # loại bỏ nút gốc ra khỏi danh sách.
                else:
                    truocGoc.keTiep = goc.keTiep
                    
            # Nếu hệ số của nút gốc không phải là 0, nó sẽ di chuyển goc tới nút kế tiếp của nó (goc = goc.keTiep) 
            # để xử lý các nút tiếp theo trong danh sách.
            goc = goc.keTiep
            if goc == self.head:
                break 
    
    def inDaThuc(self):
        tamThoi = self.head
        while True:
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
            
            if tamThoi == self.head:
                break
        print()
    
    def tich(self, daThuc2):
        traVe = DaThuc() # Tạo một đối tượng mới là traVe để lưu trữ kết quả phép nhân.
        lapPhanTu1 = self.head 
        
        while True: # Sử dụng con trỏ lapPhanTu1 để duyệt qua danh sách liên kết của đa thức thứ nhất.
            lapPhanTu2 = daThuc2.head
            while True:
                heSo = lapPhanTu1.heSo * lapPhanTu2.heSo
                soMu = lapPhanTu1.soMu + lapPhanTu2.soMu
                traVe.them(heSo, soMu)
                lapPhanTu2 = lapPhanTu2.keTiep
                if lapPhanTu2 == daThuc2.head:
                    break
            lapPhanTu1 = lapPhanTu1.keTiep
            if lapPhanTu1 == self.head:
                break
            
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