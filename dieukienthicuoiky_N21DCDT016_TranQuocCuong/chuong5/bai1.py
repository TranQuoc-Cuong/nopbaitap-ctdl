class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None 
        self.phai = None 

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.goc = None # Gốc của cây, ban đầu được khởi tạo là None.

    def SoNut(self, node):
        if node is None: # Nếu node là None, trả về 0 (cây rỗng hoặc đã đến cuối nhánh).
            return 0
        else:
            soNutConBenTrai = self.SoNut(node.trai)
            soNutConBenPhai = self.SoNut(node.phai)
            return soNutConBenTrai + soNutConBenPhai + 1 # Tổng số nút là tổng của nút bên trái, nút bên phải và chính nút hiện tại (+ 1).

# Tạo một cây nhị phân
cay = PhuongThuc()

cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(6)
cay.goc.phai.trai = TreeNode(4)
cay.goc.phai.phai = TreeNode(5)
# cấu  trúc cây        
#        1
#      /   \
#     2     3
#    /     / \
#   6     4   5

so_nut = cay.SoNut(cay.goc)

print("Số nút của cây là:", so_nut) # Kết quả sẽ là 6