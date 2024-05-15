class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        giaTris = reversed(self.list)
        giaTris = [str(x) for x in giaTris]
        return ' '.join(giaTris)

    def push(self, giaTri):
        self.list.append(giaTri)
        return 

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

    def inNguocDeQuy(self):
        if self.head is None:
            return
        else:
            self.innguoc_dequy(self.head)
    
    def innguoc_dequy(self, nut):
        if nut.next is not None:
            self.innguoc_dequy(nut.next) # Gọi đệ quy đến cuối danh sách trước khi in thông tin info của nut.
            print(nut.info, end=" ")
        else:
            print(nut.info, end=" ")

    def inNguocStack(self):
        xepChong = Stack()
        lapPhanTu = self.head
        while lapPhanTu is not None:
            xepChong.push(lapPhanTu.info)
            lapPhanTu = lapPhanTu.next
        print(xepChong)


    def inDanhSach(self): # In tất cả các phần tử trong danh sách theo thứ tự từ đầu đến cuối.
        lapPhanTu = self.head
        while lapPhanTu is not None:
            print(lapPhanTu.info, end=" ")
            lapPhanTu = lapPhanTu.next
        print()

# Tạo danh sách liên kết
dslk = DanhSachLienKet()
dslk.them(9)
dslk.them(8)
dslk.them(7)
dslk.them(6)
dslk.them(5)

# In danh sách liên kết
print("Danh sách liên kết: ", end='')
dslk.inDanhSach()

# In ngược danh sách liên kết bằng phương pháp đệ qui
print("In ngược danh sách (đệ qui): ", end='')
dslk.inNguocDeQuy()

print()
print("In ngược danh sách (Stack): ", end='')
dslk.inNguocStack()
