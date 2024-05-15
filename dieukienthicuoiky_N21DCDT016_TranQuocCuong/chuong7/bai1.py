class DoThi:
    def __init__(self):
        self.ds_ke = {}  # Danh sách kề (adjacency list)

    def themCanh(self, u, v):
        if u not in self.ds_ke:
            self.ds_ke[u] = []
        if v not in self.ds_ke:
            self.ds_ke[v] = []
        self.ds_ke[u].append(v)
        self.ds_ke[v].append(u)  # Nếu là đồ thị vô hướng

    def DFS(self, v, chiden):
        chiden[v] = True
        for neighbour in self.ds_ke[v]:
            if not chiden[neighbour]:
                self.DFS(neighbour, chiden)

    def lienThong(self):
        chiden = {v: False for v in self.ds_ke}  # Khởi tạo tất cả các đỉnh đều chưa được thăm
        start_vertex = next(iter(self.ds_ke)) # Bắt đầu duyệt từ đỉnh đầu tiên trong danh sách
        self.DFS(start_vertex, chiden)        
        for vertex in chiden: # Kiểm tra tất cả các đỉnh đã được thăm hay chưa
            if not chiden[vertex]:
                return False
        return True

dt = DoThi()
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(3, 4)

print(dt.lienThong())  # Kết quả sẽ là False

dt.themCanh(2, 3)  # Nếu thêm cạnh này thì đồ thị sẽ liên thông
print(dt.lienThong())