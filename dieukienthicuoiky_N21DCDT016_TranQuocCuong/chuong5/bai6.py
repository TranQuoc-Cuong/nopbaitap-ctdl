class TreeNode:
    def __init__(self, info): 
        self.info = info
        self.trai = None
        self.phai = None

class PhuongThuc:
    def __init__(self):
        self.goc = None 

    def kiemTraAVL(self, node):
        return self._kiemTraAVL(node) != -1

    def _kiemTraAVL(self, node):
        if node is None:
            return 0

        trai_chieucao = self._kiemTraAVL(node.trai)
        if trai_chieucao == -1: # Nếu chiều cao của cây con bên trái là -1 thì trả về -1 (cây không cân bằng)
            return -1

        phai_chieucao = self._kiemTraAVL(node.phai) # Gọi đệ quy để kiểm tra chiều cao của cây con bên phải
        if phai_chieucao == -1: # Nếu chiều cao của cây con bên phải là -1 thì trả về -1 (cây không cân bằng)
            return -1

        if abs(trai_chieucao - phai_chieucao) > 1:  # Nếu sự chênh lệch giữa chiều cao của cây con bên trái và bên phải lớn hơn 1 thì trả về -1 (cây không cân bằng)
            return -1

        return max(trai_chieucao, phai_chieucao) + 1  # Trả về chiều cao lớn nhất của cây con và cộng thêm 1 (tính cả nút hiện tại)


# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(4)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(6)
cay.goc.trai.trai = TreeNode(1)
cay.goc.trai.phai = TreeNode(3)
cay.goc.phai.trai = TreeNode(5)
cay.goc.phai.phai = TreeNode(7)

# Gọi phương thức kiemTraAVL() để kiểm tra xem cây có phải là cây AVL hay không
is_avl = cay.kiemTraAVL(cay.goc)

# In kết quả
if is_avl:
    print("Cây là một cây AVL")
else:
    print("Cây không phải là cây AVL")