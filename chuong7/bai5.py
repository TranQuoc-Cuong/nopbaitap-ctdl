class DoThi:
    def __init__(self):
        self.ds_ke = {}  # Danh sách kề (adjacency list)

    def themCanh(self, u, v):
        if u not in self.ds_ke:
            self.ds_ke[u] = []
        if v not in self.ds_ke:
            self.ds_ke[v] = []
        self.ds_ke[u].append(v)
        self.ds_ke[v].append(u)  # Đồ thị vô hướng nên thêm cả hai chiều

    def chuaDinh(self, v):
        return v in self.ds_ke

    def bacDinh(self, v):
        if v not in self.ds_ke:
            return None  # Đỉnh không tồn tại trong đồ thị
        return len(self.ds_ke[v])

# Ví dụ sử dụng
dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)

print(dt.bacDinh(0))  # Kết quả sẽ là 2 vì đỉnh 0 nối với 1 và 2
print(dt.bacDinh(2))  # Kết quả sẽ là 3 vì đỉnh 2 nối với 0, 1 và 3
print(dt.bacDinh(4))  # Kết quả sẽ là None vì đỉnh 4 không tồn tại trong đồ thị