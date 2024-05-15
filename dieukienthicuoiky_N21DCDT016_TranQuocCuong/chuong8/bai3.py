# Định nghĩa lớp Album và lớp Bài Hát
class BaiHat:
    def __init__(self, ten_bai_hat, nhac_si, ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.nhac_si = nhac_si
        self.ca_si = ca_si
    
    def __repr__(self):
        return f"{self.ten_bai_hat} - {self.nhac_si} (Ca Sĩ: {self.ca_si})"
    
class Album:
    def __init__(self, ten_album):
        self.ten_album = ten_album
        self.bai_hat = []
        
    def them_bai_hat(self, ten_bai_hat, nhac_si, ca_si):
        self.bai_hat.append(BaiHat(ten_bai_hat, nhac_si, ca_si))
        
    def __repr__(self):
        bai_hat_str = "\n".join(str(bh) for bh in self.bai_hat)
        return f"Album: {self.ten_album}\n Bài hát {bai_hat_str}"
    
class TuDien:
    def __init__(self):
        # Bảng băm cho các album, với tên album làm khóa
        self.table = {}

    def NhapAlbum(self, album):
        # Nhập thông tin album vào từ điển
        if album.ten_album in self.table:
            print(f"Album '{album.ten_album}' đã tồn tại!")
        else:
            self.table[album.ten_album] = album
            
    def XemAlbum(self,ten_album):
         # Tra cứu thông tin album theo tên
        if ten_album in self.table:
            return self.table[ten_album]
        else:
            return f"Album '{ten_album}' không tồn tại."
        
# Tạo từ điển album
td = TuDien()

# Tạo và thêm album đầu tiên
album1 = Album("Những Bài Nhạc Trẻ")
album1.them_bai_hat("Đường Tôi Chở Em Về", "Tú Dưa", "buitruonglinh")
album1.them_bai_hat("Tháng Tư Là Lời Nói Dối Của Em", "Hà Anh Tuấn", "Hà Anh Tuấn")

td.NhapAlbum(album1)

# Tạo và thêm album thứ hai
album2 = Album("Những Bài Ca Mùa Hè")
album2.them_bai_hat("Bài Ca Mùa Hè", "Trần Văn C", "Mỹ Linh")
album2.them_bai_hat("Mùa Hè Xanh", "Nguyễn Văn D", "Hà Anh Tuấn")

td.NhapAlbum(album2)

# Xem thông tin về album
album_xem = td.XemAlbum("Những Bài Nhạc Trẻ")
print(album_xem)

album_xem2 = td.XemAlbum("Những Bài Ca Mùa Hè")
print(album_xem2)

# Thử xem album không tồn tại
album_khong_ton_tai = td.XemAlbum("Không Tồn Tại")
print(album_khong_ton_tai)


    