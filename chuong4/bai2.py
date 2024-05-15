class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        giaTris = reversed(self.list)
        giaTris = [str(x) for x in giaTris]
        return ' '.join(giaTris)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, giaTri):
        self.list.append(giaTri)
        return self
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop()
        
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class DanhSachLienKet:
    def __init__(self):
        self.head = None 

    def them(self, info): 
        nut = Node(info)
        if self.head is None: # Nếu danh sách rỗng
            self.head = nut  # head sẽ là nut mới
        else:
            lapPhanTu = self.head
            while lapPhanTu.next is not None: 
                lapPhanTu = lapPhanTu.next
            lapPhanTu.next = nut

    def daoNguoc(self):
        xepChong = Stack()
        lapPhanTu = self.head
        while lapPhanTu is not None:
            xepChong.push(lapPhanTu.info)  # Push giaTri, not Node
            lapPhanTu = lapPhanTu.next

        if not xepChong.isEmpty():
            self.head = Node(xepChong.pop())  # Tạo Node mới cho head từ giá trị đầu tiên
            lapPhanTu = self.head
            while not xepChong.isEmpty():
                giaTri = xepChong.pop()  # Pop giá trị từ Stack
                nutMoi = Node(giaTri)  # Tạo Node mới từ giá trị
                lapPhanTu.next = nutMoi  # Nối Node mới vào danh sách
                lapPhanTu = nutMoi  # Cập nhật lapPhanTu

    def InDanhSach(self): # In tất cả các phần tử trong danh sách theo thứ tự từ đầu đến cuối.
        lapPhanTu = self.head
        while lapPhanTu is not None:
            print(lapPhanTu.info, end=" ")
            lapPhanTu = lapPhanTu.next
        print()

dslk = DanhSachLienKet()
dslk.them(1)
dslk.them(2)
dslk.them(3)
dslk.them(4)
dslk.InDanhSach()

dslk.daoNguoc()
dslk.InDanhSach()