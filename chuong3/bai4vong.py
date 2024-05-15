class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo
        self.soMu = soMu
        self.keTiep = None  #  một tham chiếu tới nút tiếp theo trong danh sách (keTiep).

class DaThuc:
    def __init__(self):
        self.head = None

    def them(self, heSoMoi, soMuMoi): # thêm một hạng tử mới vào đa thức theo thứ tự giảm dần của số mũ.
            nutMoi = Node(heSoMoi, soMuMoi)
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
    
    def doiDau(self):
        current = self.head
        while True:
            current.heSo = -current.heSo
            current = current.keTiep
            if current == self.head:
                break
        
# Tạo đa thức
dathuc = DaThuc()
dathuc.them(4, 3)
dathuc.them(-5, 2)
dathuc.them(2, 1)
dathuc.them(6, 0)

dathuc.inDaThuc()  


dathuc.doiDau()

dathuc.inDaThuc()  