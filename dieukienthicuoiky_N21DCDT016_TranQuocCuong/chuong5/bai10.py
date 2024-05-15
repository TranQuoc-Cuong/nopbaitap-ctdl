class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None
        self.phai = None 

class PhuongThuc: 
    def __init__(self):
        self.goc = None 

    def canBangHoanToan(self): # Phương thức này được gọi từ bên ngoài và kiểm tra xem cây nhị phân có cân bằng hoàn toàn hay không.
        return self._canBangHoanToan(self.goc) # Nó bắt đầu kiểm tra từ gốc của cây.

    def _canBangHoanToan(self, node):  # Phương thức đệ quy để kiểm tra xem cây nhị phân con có cân bằng hoàn toàn hay không.
        if node is None:
            return True  # Nếu nút hiện tại là None, nghĩa là cây con này không tồn tại và do đó được xem là cân bằng.
        trai_subtree_count = self._DemNut(node.trai)    # Đếm số nút trong cây con bên trái.
        phai_subtree_count = self._DemNut(node.phai)    # Đếm số nút trong cây con bên phải.
        if abs(trai_subtree_count - phai_subtree_count) > 1:  # Kiểm tra sự chênh lệch số lượng nút giữa cây con bên trái và bên phải.
            return False  # Nếu sự chênh lệch lớn hơn 1, cây không cân bằng hoàn toàn.
        return self._canBangHoanToan(node.trai) and self._canBangHoanToan(node.phai)  # Tiếp tục kiểm tra đệ quy cho cây con bên trái và bên phải.

    def _DemNut(self, node):
        if node is None: # Phương thức đệ quy để đếm tổng số nút trong cây con.
            return 0  # Nếu nút hiện tại là None, trả về 0 vì không có nút nào ở cây con này.
        return 1 + self._DemNut(node.trai) + self._DemNut(node.phai) # Đếm nút hiện tại (1) cộng với tổng số nút trong cây con bên trái và cây con bên phải.


# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = TreeNode(1)
cay.goc.trai = TreeNode(2)
cay.goc.phai = TreeNode(3)
cay.goc.trai.trai = TreeNode(4)
cay.goc.trai.phai = TreeNode(5)
cay.goc.phai.trai = TreeNode(6)
cay.goc.phai.phai = TreeNode(7)

# Kiểm tra cây nhị phân có cân bằng hoàn toàn hay không
is_balanced = cay.canBangHoanToan()

# In kết quả
if is_balanced:
    print("Cây nhị phân là cây cân bằng hoàn toàn")
else:
    print("Cây nhị phân không là cây cân bằng hoàn toàn")