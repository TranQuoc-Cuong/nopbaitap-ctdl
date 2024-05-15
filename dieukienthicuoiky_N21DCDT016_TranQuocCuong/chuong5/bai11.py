class Node:
    def __init__(self, info):
        self.info = info
        self.trai = None 
        self.phai = None

class PhuongThuc:
    def __init__(self):
        self.goc = None

    def bstTuanTu(self):  # Gọi phương thức _bstTuanTu() với node gốc (self.goc)
        if self._bstTuanTu(self.goc): # Nếu kết quả trả về True, in ra thông báo cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự
            print("Cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")
        else: # Nếu kết quả trả về False, in ra thông bá
            print("Cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")  # o cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự

    def _bstTuanTu(self, node):
        # Nếu node hiện tại là None (đã duyệt hết cây hoặc cây rỗng), trả về True
        if node is None:
            return True

        # Nếu node có cả con trái và con phải không phải là None (tức là node có cả 2 con), trả về False
        if node.trai and node.phai is not None:
            return False

        # Gọi đệ quy để kiểm tra cây con bên trái và cây con bên phải
        return self._bstTuanTu(node.trai) and self._bstTuanTu(node.phai)


# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.goc = Node(4)
cay.goc.trai = Node(2)
cay.goc.trai.trai = Node(1)

# Kiểm tra cây nhị phân có thỏa mãn tính chất của cây BST và tìm kiếm tuần tự hay không
is_bst_tuantu = cay.bstTuanTu()