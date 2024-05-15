class Mang:
    def __init__(self, matran):
        self.matran = matran
            
    def _DienTich(self, matran, decap, dong, cot):
        # Kiểm tra giới hạn của ma trận và trạng thái đã thăm
        if dong < 0 or cot < 0 or dong >= len(matran) or cot >= len(matran[0]) or decap[dong][cot] or matran[dong][cot] == 0:
            return 0

        # Đánh dấu ô đã thăm
        decap[dong][cot] = True

        # Đệ quy kiểm tra các ô kề cạnh
        dem = 1
        dem += self._DienTich(matran, decap, dong + 1, cot)  # Kiểm tra ô phía dưới
        dem += self._DienTich(matran, decap, dong - 1, cot)  # Kiểm tra ô phía trên
        dem += self._DienTich(matran, decap, dong, cot + 1)  # Kiểm tra ô bên phải
        dem += self._DienTich(matran, decap, dong, cot - 1)  # Kiểm tra ô bên trái
        return dem


    def Dao(self):
        dongs = len(self.matran)
        cots = len(self.matran[0])

        dientichlonnhat = 0  # Diện tích lớn nhất của các đảo hình chữ nhật

        # Tạo ma trận decap để lưu trạng thái đã thăm
        decap = [[False for _ in range(cots)] for _ in range(dongs)]

        for dong in range(dongs):
            for cot in range(cots):
                # có được đánh dấu đã thăm chưa (decap[dong][cot]), và có phải là đất liền không (matran[dong][cot] == 0)
                if not decap[dong][cot] and self.matran[dong][cot] == 1:
                    area = self._DienTich(self.matran, decap, dong, cot)
                    dientichlonnhat = max(dientichlonnhat, area)

        return dientichlonnhat

mang = Mang([[1, 0, 1, 1, 0],
             [1, 1, 0, 0, 1],
             [0, 1, 0, 1, 1],
             [0, 0, 0, 1, 1],
             [1, 1, 1, 0, 1]])

print(mang.Dao()) 