class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None
        self.phai = None

class PhuongThuc: 
    def __init__(self):
        self.goc = None # Gốc của cây, ban đầu được khởi tạo là None.

    def soNutLa(self, node):
            if node is None: 
                return 0
            if node.trai is None and node.phai is None: # Nếu nút không có con thì đó là nút lá
                return 1
            else:
                trai_dem = self.soNutLa(node.trai)
                phai_dem = self.soNutLa(node.phai)
                return trai_dem + phai_dem

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(4)
cay.goc.trai.phai = TreeNode(5)
cay.goc.phai.trai = TreeNode(6)

#        1
#       /  \
#      2    3
#     / \   /
#    4   5 6   
#
# Gọi phương thức soNutLa() để đếm số nút lá
so_nut_la = cay.soNutLa(cay.goc)

print("Số nút lá của cây là:", so_nut_la)