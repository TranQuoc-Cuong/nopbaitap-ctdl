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

    def DFSVoHuong(self, v, chiden, parent):
        chiden[v] = True
        for neighbour in self.ds_ke[v]:
            if not chiden[neighbour]:
                if self.DFSVoHuong(neighbour, chiden, v):
                    return True
            elif neighbour != parent:
                return True
        return False

    def DFSHuuHuong(self, v, chiden, rec_stack):
        chiden[v] = True
        rec_stack[v] = True
        for neighbour in self.ds_ke[v]:
            if not chiden[neighbour]:
                if self.DFSHuuHuong(neighbour, chiden, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    def ChuTrinh(self):
        chiden = {v: False for v in self.ds_ke}
        if self.huong:
            rec_stack = {v: False for v in self.ds_ke}
            for vertex in self.ds_ke:
                if not chiden[vertex]:
                    if self.DFSHuuHuong(vertex, chiden, rec_stack):
                        return True
        else:
            for vertex in self.ds_ke:
                if not chiden[vertex]:
                    if self.DFSVoHuong(vertex, chiden, -1):
                        return True
        return False

# Ví dụ sử dụng cho đồ thị vô hướng
dt_vo_huong = DoThi(huong=False)
dt_vo_huong.themCanh(0, 1)
dt_vo_huong.themCanh(1, 2)
dt_vo_huong.themCanh(2, 0)

print(dt_vo_huong.ChuTrinh())  # Kết quả sẽ là True vì có chu trình

# Ví dụ sử dụng cho đồ thị hữu hướng
dt_huu_huong = DoThi(huong=True)
dt_huu_huong.themCanh(0, 1)
dt_huu_huong.themCanh(1, 2)
dt_huu_huong.themCanh(2, 0)

print(dt_huu_huong.ChuTrinh())  # Kết quả sẽ là True vì có chu trình