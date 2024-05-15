class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None 
        self.phai = None

class PhuongThuc:
    def __init__(self):
        self.goc = None 
        
    def chep(self):
        return self._chep(self.goc)  # Gọi phương thức đệ quy _chep() để sao chép cây nhị phân, bắt đầu từ nút gốc (self.goc)

    def _chep(self, node):
        if node is None:  # Nếu nút hiện tại là None, trả về None (điểm dừng của đệ quy)
            return None

        new_node = TreeNode(node.info) # Tạo một nút mới với thông tin của nút hiện tại
        new_node.trai = self._chep(node.trai) # Sao chép cây con bên trái của nút hiện tại và gán cho cây con bên trái của nút mới
        new_node.phai = self._chep(node.phai) # Sao chép cây con bên phải của nút hiện tại và gán cho cây con bên phải của nút mới
        
        return new_node # Trả về nút mới đã được sao chép


# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(4)
cay.goc.trai.phai = TreeNode(5)

# Sao chép cây nhị phân
copied_cay = cay.chep()

# Dùng đệ quy để in cây BST
def inOrder(node):
    if node.trai is None or node.phai is None:
        print(node.info, end=" ")
    else:
        inOrder(node.trai)
        inOrder(node.phai)
        print(node.info, end=" ")

# In cây nhị phân ban đầu
print("Cây nhị phân ban đầu:")
inOrder(cay.goc)
print()

# In cây nhị phân đã sao chép
print("Cây nhị phân đã sao chép:")
inOrder(copied_cay)