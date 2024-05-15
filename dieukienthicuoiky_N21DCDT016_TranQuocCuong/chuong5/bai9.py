class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None
        self.phai = None 

class PhuongThuc: 
    def __init__(self):
        self.goc = None 

    def cayCon(self, cayKhac):
        if self._cayCon(self.goc, cayKhac.goc):
            print("Cây nhị phân thứ hai là cây con của cây nhị phân thứ nhất")
        else:
            print("Cây nhị phân thứ hai không là cây con của cây nhị phân thứ nhất")

    def _cayCon(self, node1, node2):
        # Nếu cả hai node đều là None, điều này có nghĩa là cả hai cây đều đã kết thúc tại đây và chúng là giống nhau
        if node1 is None and node2 is None:
            return True

        # Nếu node1 là None nhưng node2 không phải là None, điều này có nghĩa là cayKhac lớn hơn hoặc khác nhau
        if node1 is None and node2 is not None:
            return False

        # Nếu node1 không phải là None nhưng node2 là None, điều này có nghĩa là cây hiện tại chứa cayKhac như là cây con
        if node1 is not None and node2 is None:
            return True

        # Nếu thông tin của node hiện tại của cả hai cây không giống nhau, chúng không thể là cây con
        if node1.info != node2.info:
            return False

        # Kiểm tra đệ quy cho cây con bên trái và bên phải
        trai_result = self._cayCon(node1.trai, node2.trai)
        phai_result = self._cayCon(node1.phai, node2.phai)

        # Trả về kết quả kiểm tra của cây con bên trái hoặc bên phải
        return trai_result or phai_result

# Tạo hai cây nhị phân
cay1 = PhuongThuc()
cay2 = PhuongThuc()

# Xây dựng cây nhị phân thứ nhất
cay1.goc = TreeNode(1)
cay1.goc.trai = TreeNode(2)
cay1.goc.phai = TreeNode(3)
cay1.goc.trai.trai = TreeNode(4)
cay1.goc.trai.phai = TreeNode(5)

# Xây dựng cây nhị phân thứ hai
cay2.goc = TreeNode(2)
cay2.goc.trai = TreeNode(4)
cay2.goc.phai = TreeNode(5)

# Kiểm tra cây nhị phân thứ hai có là cây con của cây nhị phân thứ nhất hay không
is_subtree = cay1.cayCon(cay2)

# In kết quả