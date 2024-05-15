class DoThi:
    def __init__(self, huong=False):
        self.ds_ke = {}  # Danh sách kề (adjacency list)
        self.huong = huong  # Biến để xác định đồ thị có hướng hay không

    def themCanh(self, u, v):
        if u not in self.ds_ke:
            self.ds_ke[u] = []
        if v not in self.ds_ke:
            self.ds_ke[v] = []
        self.ds_ke[u].append(v)
        if not self.huong:
            self.ds_ke[v].append(u)

    def chuaDinh(self, v):
        return v in self.ds_ke

    def soCungVao(self, v):
        if not self.huong:
            return None  # Phương thức chỉ áp dụng cho đồ thị hữu hướng
        dem = 0
        for u in self.ds_ke:
            if v in self.ds_ke[u]:
                dem += 1
        return dem

# Ví dụ sử dụng
dt_huu_huong = DoThi(huong=True)
dt_huu_huong.themCanh(0, 1)
dt_huu_huong.themCanh(2, 1)
dt_huu_huong.themCanh(3, 1)
dt_huu_huong.themCanh(1, 2)

print(dt_huu_huong.soCungVao(1))  # Kết quả sẽ là 3 vì có 3 cung đi vào đỉnh 1 (từ 0, 2, và 3)
print(dt_huu_huong.soCungVao(2))  # Kết quả sẽ là 1 vì có 1 cung đi vào đỉnh 2 (từ 1)
print(dt_huu_huong.soCungVao(3))  # Kết quả sẽ là 0 vì không có cung nào đi vào đỉnh 3