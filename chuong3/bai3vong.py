class Node:
    def __init__(self, heSo, soMu):
        self.heSo = heSo
        self.soMu = soMu
        self.keTiep = None #  một tham chiếu tới nút tiếp theo trong danh sách (keTiep).
        
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
        gocTruoc = goc # nút gocTruoc là nút goc trước đó 
        while True:
            timKiem = goc.keTiep
            while True: # bắt đầu bằng cách duyệt qua từng nút trong danh sách
                if timKiem.soMu == goc.soMu: # Nếu tìm thấy một nút với số mũ giống nhau
                    goc.heSo += timKiem.heSo # cộng hệ số của nút đó vào hệ số của nút gốc
                    goc.keTiep = timKiem.keTiep #  loại bỏ nút đó ra khỏi danh sách
                timKiem = timKiem.keTiep
                if timKiem == goc:
                    break
                
            # Sau khi duyệt qua tất cả các nút
            if goc.heSo == 0: # kiểm tra xem hệ số của nút goc có bằng 0 không. Nếu có loại bỏ nút đó khỏi danh sách
                # Nếu goc.keTiep is None,tức là goc là nút cuối cùng của danh sách, 
                # nó sẽ chỉnh sửa tham chiếu từ nút trước đó (gocTruoc) để trỏ tới None, loại bỏ nút goc ra khỏi danh sách.
                if goc.keTiep == self.head: 
                    gocTruoc.keTiep = None 
                    
                # Nếu goc == self.head, tức là goc là nút đầu tiên của danh sách, 
                # nó sẽ chỉnh sửa self.head để trỏ tới nút kế tiếp của goc (goc.keTiep), và sau đó di chuyển tham chiếu gocTruoc tới self.head.
                elif goc == self.head:
                    goc_cu = goc # lưu lại giá trị gốc cũ
                    self.head = goc.keTiep # thay đổi head của node bằng giá trị tiếp theo
                    gocTruoc = self.head   # cho gocTruoc về head của node
                    tamThoi = self.head # vì ta đã bỏ đi gốc cũ nên cần phải thay đổi giá trị kế tiếp của node cuối cùng 
                    while True:
                        tamThoi = tamThoi.keTiep # trỏ đến node kế tiếp
                        if tamThoi.keTiep == goc_cu: # nếu node kế tiếp chỉ đến giá trị của goc_cu (là gốc mà ta đã xóa)
                            break
                    tamThoi.keTiep == self.head # thay đổi giá trị của node kế tiếp về lại giá trị head mới
                
                # Trong trường hợp còn lại, 
                # nó chỉnh sửa tham chiếu của nút trước đó (gocTruoc) để trỏ tới nút kế tiếp của goc (goc.keTiep), 
                # loại bỏ nút gốc ra khỏi danh sách.
                else:
                    gocTruoc.keTiep = goc.keTiep
                
                tamThoi.keTiep = self.head
                    
            # Nếu hệ số của nút gốc không phải là 0, nó sẽ di chuyển goc tới nút kế tiếp của nó (goc = goc.keTiep) 
            # để xử lý các nút tiếp theo trong danh sách.
            goc = goc.keTiep
            if goc == self.head:
                break 

    def cong(self, daThuc2):
        traVe = DaThuc() # tạo một đối tượng mới là traVe để lưu trữ kết quả phép cộng.
        p1 = self.head
        p2 = daThuc2.head
        # Hai con trỏ p1 và p2 được sử dụng để duyệt qua hai danh sách liên kết của các hạng tử của hai đa thức.
        while True:
            # Trong quá trình duyệt, nếu hạng tử tại p1 có số mũ lớn hơn số mũ tại p2, 
            # hạng tử đó sẽ được thêm vào traVe và p1 sẽ di chuyển đến hạng tử tiếp theo.
            if p1.soMu > p2.soMu: 
                traVe.them(p1.heSo, p1.soMu)
                p1 = p1.keTiep
            # nếu hạng tử tại p2 có số mũ lớn hơn số mũ tại p1, 
            # hạng tử đó sẽ được thêm vào traVe và p2 sẽ di chuyển đến hạng tử tiếp theo.
            elif p1.soMu < p2.soMu:
                traVe.them(p2.heSo, p2.soMu)
                p2 = p2.keTiep
            else: # Nếu số mũ tại p1 và p2 bằng nhau, hệ số của hai hạng tử này sẽ được cộng lại với nhau
                heSo_sum = p1.heSo + p2.heSo
                if heSo_sum != 0: # Nếu kết quả khác 0, hạng tử mới sẽ được thêm vào traVe.
                    traVe.them(heSo_sum, p1.soMu)
                p1 = p1.keTiep
                p2 = p2.keTiep
            if p1 == self.head or p2 == daThuc2.head:
                break
                
        # Sau khi duyệt qua tất cả các hạng tử của cả hai đa thức, các hạng tử còn lại của p1 và p2 sẽ được thêm vào traVe.
        if p1 != self.head:
            while True:
                traVe.them(p1.heSo, p1.soMu)
                p1 = p1.keTiep
                if p1 == self.head:
                    break
        
        if p2 != daThuc2.head:
            while True:
                traVe.them(p2.heSo, p2.soMu)
                p2 = p2.keTiep
                if p2 == daThuc2.head:
                    break

        traVe.rutGon() # Cuối cùng dùng phương thức rutGon được gọi để rút gọn đa thức kết quả và kết quả được trả về.
        return traVe
    

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