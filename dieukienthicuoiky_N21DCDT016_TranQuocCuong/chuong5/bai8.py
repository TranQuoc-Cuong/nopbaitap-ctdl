class TreeNode:
    def __init__(self, info): 
        self.info = info 
        self.trai = None 
        self.phai = None 

class PhuongThuc:
    def __init__(self):
        self.goc = None

    def soSanh(self, cayKhac):
        if self._soSanh(self.goc, cayKhac.goc):
            print("Hai cây nhị phân giống hệt nhau")
        else:
            print("Hai cây nhị phân không giống hệt nhau")

    def _soSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        elif node1 is None or node2 is None:
            return False

        elif node1.info != node2.info:
            return False
        else:
            trai_result = self._soSanh(node1.trai, node2.trai)
            phai_result = self._soSanh(node1.phai, node2.phai)

            # Trả về True nếu cả cây con bên trái và bên phải đều giống hệt nhau
            return trai_result and phai_result


# Tạo hai cây nhị phân
cay1 = PhuongThuc()
cay2 = PhuongThuc()

# Cây nhị phân thứ nhất
cay1.goc = TreeNode(1)
cay1.goc.trai = TreeNode(2)
cay1.goc.phai = TreeNode(3)

# Cây nhị phân thứ hai
cay2.goc = TreeNode(1)
cay2.goc.trai = TreeNode(2)
cay2.goc.phai = TreeNode(3)

# So sánh hai cây nhị phân
cay1.soSanh(cay2)