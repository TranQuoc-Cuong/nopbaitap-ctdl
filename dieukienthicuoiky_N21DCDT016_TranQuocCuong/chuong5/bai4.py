class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None 
        self.phai = None 
class PhuongThuc:
    def __init__(self):
        self.goc = None

    def SoNutTrungGian(self, node):
        if node is None: # Nếu node là None, tức là cây con này không tồn tại hoặc đã đến lá, phương thức trả về 0.
            return 0
        elif node.trai is None and node.phai is None:  
            return 0
        elif node.trai is None and node.phai is None:
            return 1
        else:
            trai_dem = self.SoNutTrungGian(node.trai)
            phai_dem = self.SoNutTrungGian(node.phai)
            return trai_dem + phai_dem + 1

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(4)
cay.goc.trai.phai = TreeNode(5)

so_nut_trung_gian = cay.SoNutTrungGian(cay.goc)

print("Số nút trung gian của cây là:", so_nut_trung_gian)