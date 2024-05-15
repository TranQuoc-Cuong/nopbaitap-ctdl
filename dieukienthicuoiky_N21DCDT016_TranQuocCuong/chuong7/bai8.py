class DoThi: 
    def __init__(self, so_dinh): 
        # Khởi tạo đồ thị với số đỉnh
        self.so_dinh = so_dinh 
        self.dinh_ke = [[] for _ in range(so_dinh)] 

    def themCanh(self, v1, v2): 
        # Thêm cạnh từ v1 đến v2 (và ngược lại nếu là đồ thị vô hướng)
        self.dinh_ke[v1].append(v2) 
        # Đối với đồ thị vô hướng, bỏ comment dòng dưới
        # self.dinh_ke[v2].append(v1)

    def DFS(self, v, visited): 
        # Đánh dấu đỉnh hiện tại là đã thăm
        visited[v] = True

        # Nhận tất cả đỉnh kề của đỉnh hiện tại và gọi đệ quy
        for i in self.dinh_ke[v]: 
            if not visited[i]: 
                self.DFS(i, visited) 

    def duongDi(self, v1, v2): 
        # Mảng để kiểm tra viên đỉnh đã được thăm chưa
        visited = [False] * self.so_dinh 

        # Gọi DFS từ v1
        self.DFS(v1, visited) 

        # Nếu v2 được thăm, tức là có đường đi từ v1 đến v2
        return visited[v2] 

# Ví dụ sử dụng
dt = DoThi(5)  # Tạo đồ thị với 5 đỉnh
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 3)
dt.themCanh(2, 3)
dt.themCanh(3, 4)

print(dt.duongDi(0, 4))  # In ra True vì có đường đi từ đỉnh 0 đến đỉnh 4
print(dt.duongDi(4, 0))  # In ra False nếu đồ thị hướng và không có đường đi từ 4 đến 0