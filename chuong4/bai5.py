class HanoiTower:
    def __init__(self, n):
        self.n = n  # Số đĩa
        self.moves = []  # Danh sách lưu trữ các bước di chuyển

    def move(self, n, start, end, middle):
        if n == 1:
            self.moves.append((start, end))  # Di chuyển đĩa từ cọc start đến cọc end
        else:
            # Di chuyển n-1 đĩa từ cọc start đến cọc middle
            self.move(n - 1, start, middle, end)
            
            # Di chuyển đĩa thứ n từ cọc start đến cọc end
            self.moves.append((start, end))
            
            # Di chuyển n-1 đĩa từ cọc middle đến cọc end
            self.move(n - 1, middle, end, start)

    def solve(self):
        self.move(self.n, 1, 3, 2)  # Giải bài toán từ cọc 1 đến cọc 3, sử dụng cọc 2 làm trung gian
        return self.moves

# Tạo một đối tượng HanoiTower với 4 đĩa
tower = HanoiTower(4)

solution = tower.solve()

for move in solution:
    print(f"Di chuyển từ cọc {move[0]} đến cọc {move[1]}")