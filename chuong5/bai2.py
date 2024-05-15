class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None 
        self.phai = None 

class PhuongThuc: 
    def __init__(self):
        self.goc = None 

    def chieuCao(self, node):
        if node is None: 
            return 0 

        else:
            trai_chieucao = self.chieuCao(node.trai)
            phai_chieucao = self.chieuCao(node.phai) 
            return max(trai_chieucao, phai_chieucao) + 1

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(4)
cay.goc.trai.trai.trai = TreeNode(5)

#       1
#      / \
#     2   3
#    /     
#   4 
#  /
# 5      
# Gọi phương thức chieuCao() để tính chiều cao
chieu_cao = cay.chieuCao(cay.goc)

print("Chiều cao của cây là:", chieu_cao)