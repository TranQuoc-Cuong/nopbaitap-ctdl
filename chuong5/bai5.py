class TreeNode:
    def __init__(self, info):
        self.info = info 
        self.trai = None 
        self.phai = None

class PhuongThuc: 
    def __init__(self):
        self.goc = None 

    def kiemTraBST(self, node):
        is_bst = self._kiemTraBST(node)
        if is_bst:
            print("Cây là một cây BST")
        else:
            print("Cây không phải là cây BST")

    def _kiemTraBST(self, node):
        if node is None:
            return True
        
        elif node.trai is None or node.phai is None: # Nếu một trong các nút con (trái hoặc phải) là None thì trả về True
            return True
        
        elif node.trai.info >= node.info or node.info >= node.phai.info:
            return False
           
        return (self._kiemTraBST(node.trai) and self._kiemTraBST(node.phai))

cay = PhuongThuc()

cay.goc = TreeNode(4)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(6)
cay.goc.trai.trai = TreeNode(1)
cay.goc.trai.phai = TreeNode(3)
cay.goc.phai.trai = TreeNode(5)
cay.goc.phai.phai = TreeNode(7)

# Gọi phương thức kiemTraBST() để kiểm tra xem cây có phải là BST hay không
cay.kiemTraBST(cay.goc)

cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)

cay.kiemTraBST(cay.goc)