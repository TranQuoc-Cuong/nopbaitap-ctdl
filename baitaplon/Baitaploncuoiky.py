import re
import os

class DinhNghia:
    def __init__(self, loaiTu = None, nghia = None, viDu = None):
        self.loaiTu = loaiTu
        self.nghia = nghia
        self.viDu = viDu

class AVLNode:
    def __init__(self, tu):
        self.tu = tu
        self.cacDinhNghia = []
        self.tuTrai = None
        self.tuPhai = None
        self.cao =  1
    
    def themCacDinhNghia(self, dinhNghia):
        self.cacDinhNghia.append(dinhNghia)

def preOrderTraversal(tuGoc):
    if not tuGoc:
        return
    print(tuGoc.tu, end=' ')
    if tuGoc.cacDinhNghia:
        for d in tuGoc.cacDinhNghia:
            print("- {} | {} | {}".format(d.loaiTu, d.nghia, d.viDu))
    print()
    preOrderTraversal(tuGoc.tuTrai)
    preOrderTraversal(tuGoc.tuPhai)

def timTu(tuGoc, giaTri):
    if not tuGoc:
        return None
    if tuGoc.tu == giaTri:
        return tuGoc
    elif giaTri < tuGoc.tu:
        return timTu(tuGoc.tuTrai, giaTri)
    else:
        return timTu(tuGoc.tuPhai, giaTri)

def layChieuCao(tuGoc):
    if not tuGoc:
        return 0
    return tuGoc.cao

def quayPhai(nutMatCanBang):
    nutMoi = nutMatCanBang.tuTrai
    nutMatCanBang.tuTrai = nutMatCanBang.tuTrai.tuPhai
    nutMoi.tuPhai = nutMatCanBang
    nutMatCanBang.cao = 1 + max(layChieuCao(nutMatCanBang.tuTrai), layChieuCao(nutMatCanBang.tuPhai))
    nutMoi.cao = 1 + max(layChieuCao(nutMoi.tuTrai), layChieuCao(nutMoi.tuPhai))
    return nutMoi

def quayTrai(nutMatCanBang):
    nutMoi = nutMatCanBang.tuPhai
    nutMatCanBang.tuPhai = nutMatCanBang.tuPhai.tuTrai
    nutMoi.tuTrai = nutMatCanBang
    nutMatCanBang.cao = 1 + max(layChieuCao(nutMatCanBang.tuTrai), layChieuCao(nutMatCanBang.tuPhai))
    nutMoi.cao = 1 + max(layChieuCao(nutMoi.tuTrai), layChieuCao(nutMoi.tuPhai))
    return nutMoi

def canBangCay(tuGoc):
    if not tuGoc:
        return 0
    return layChieuCao(tuGoc.tuTrai) - layChieuCao(tuGoc.tuPhai)

def chenTu(tuGoc, nutMoi):
    if not tuGoc:
        return nutMoi
    elif nutMoi.tu < tuGoc.tu:
        tuGoc.tuTrai = chenTu(tuGoc.tuTrai, nutMoi)
    else:
        tuGoc.tuPhai = chenTu(tuGoc.tuPhai, nutMoi)
    
    tuGoc.cao = 1 + max(layChieuCao(tuGoc.tuTrai), layChieuCao(tuGoc.tuPhai))
    canBang = canBangCay(tuGoc)
    if canBang > 1 and nutMoi.tu < tuGoc.tuTrai.tu:
        return quayPhai(tuGoc)
    if canBang > 1 and nutMoi.tu > tuGoc.tuTrai.tu:
        tuGoc.tuTrai = quayTrai(tuGoc.tuTrai)
        return quayPhai(tuGoc)
    if canBang < -1 and nutMoi.tu > tuGoc.tuPhai.tu:
        return quayTrai(tuGoc)
    if canBang < -1 and nutMoi.tu < tuGoc.tuPhai.tu:
        tuGoc.tuPhai = quayPhai(tuGoc.tuPhai)
        return quayTrai(tuGoc)
    return tuGoc

def layGiaTriTuNhoNhat(tuGoc):
    if tuGoc is None or tuGoc.tuTrai is None:
        return tuGoc
    return layGiaTriTuNhoNhat(tuGoc.tuTrai)

def xoaTu(tuGoc, giaTri):
    if not tuGoc:
        return tuGoc
    elif giaTri < tuGoc.tu:
        tuGoc.tuTrai = xoaTu(tuGoc.tuTrai, giaTri)
    elif giaTri > tuGoc.tu:
        tuGoc.tuPhai = xoaTu(tuGoc.tuPhai, giaTri)
    else:
        if tuGoc.tuTrai is None:
            tam = tuGoc.tuPhai
            tuGoc = None
            return tam
        elif tuGoc.tuPhai is None:
            tam = tuGoc.tuTrai
            tuGoc = None
            return tam
        
        tam = layGiaTriTuNhoNhat(tuGoc.tuPhai)
        tuGoc.tu = tam.tu
        tuGoc.cacDinhNghia = tam.cacDinhNghia
        tuGoc.tuPhai = xoaTu(tuGoc.tuPhai, tam.tu)
    canBang = canBangCay(tuGoc)
    if canBang > 1 and canBangCay(tuGoc.tuTrai) >= 0:
        return quayPhai(tuGoc)
    if canBang < -1 and canBangCay(tuGoc.tuPhai) <= 0:
        return quayTrai(tuGoc)
    if canBang > 1 and canBangCay(tuGoc.tuTrai) < 0:
        tuGoc.tuTrai = quayTrai(tuGoc.tuTrai)
        return quayPhai(tuGoc)
    if canBang < -1 and canBangCay(tuGoc.tuPhai) > 0:
        tuGoc.tuPhai = quayPhai(tuGoc.tuPhai)
        return quayTrai(tuGoc)
    return tuGoc

def tiepTuc():
    nhap = input("Nhấn t để lặp lại chức năng, hoặc nhấn enter để quay lại menu: ")
    return nhap

def hienMenu():
    global cayTuDien
    while True:
        os.system('cls')  
        print("MENU CHƯƠNG TRÌNH TỪ ĐIỂN:")
        print("1. Thêm một mục từ của từ điển")
        print("2. Loại bỏ một mục từ của từ điển")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển")
        print("4. Lưu từ điển vào các tập tin")
        print("5. Nạp từ điển từ các tập tin")
        print("6. Kết thúc chương trình")
        chon = input("Vui lòng chọn một chức năng: ")

        if chon == '1':
            os.system('cls')
            themMotMucTu()
        elif chon == '2':
            os.system('cls')
            loaiBoMotMucTu()
        elif chon == '3':
            os.system('cls')
            traCuuCacNghiaCuaMotMucTu()
        elif chon == '4':
            os.system('cls')
            luuTuDienVaoCacTapTin()
        elif chon == '5':
            os.system('cls')
            napTuDienTuCacTapTin()
        elif chon == '6':
            os.system('cls')
            print("Chương trình kết thúc")
            return
        else:
            print('Lựa chọn không hợp lệ, vui lòng chọn lại!')

def kiemTraNhapLieu():
    pattern = re.compile("^[A-Za-z'\s,.!()0;]*$")
    nhap = input()

    while not pattern.match(nhap):
        nhap = input("Nhập liệu không hợp lệ. Chỉ nhập chữ (chữ thường). Vui lòng nhập lại, hoặc gõ số 0 để quay lại: ")
    
    return str(nhap)

def themMotMucTu():
    global cayTuDien
    preOrderTraversal(cayTuDien)
    print()
    print("Nhập từ bạn muốn, hoặc gõ số 0 để quay lại: ", end='')
    tu = kiemTraNhapLieu()
    if tu == '0':
        return
    if tu:
        if timTu(cayTuDien, tu):
            print("Từ đã tồn tại")
        else:
            nutMoi = AVLNode(tu)

            cacdinhnghiamoi = DinhNghia()
            print("Loại từ gì: ", end='')
            cacdinhnghiamoi.loaiTu = kiemTraNhapLieu()

            print("Nghĩa của từ: ", end='')
            cacdinhnghiamoi.nghia = kiemTraNhapLieu()

            print("Ví dụ: ", end='')
            cacdinhnghiamoi.viDu = kiemTraNhapLieu()

            nutMoi.themCacDinhNghia(cacdinhnghiamoi)
            cayTuDien = chenTu(cayTuDien, nutMoi) 
    
    if tiepTuc() == 't':
        os.system('cls')
        themMotMucTu()

def loaiBoMotMucTu():
    global cayTuDien
    preOrderTraversal(cayTuDien)
    print()
    print("Bạn muốn xóa từ nào, hoặc gõ số 0 để quay lại: ", end='')
    tu = kiemTraNhapLieu()
    if tu == '0':
        return
    while timTu(cayTuDien, tu) is None:
        print("Từ bạn nhập không có trong từ điển. Vui lòng nhập lại, hoặc gõ số 0 để quay lại: ", end='')
        tu = kiemTraNhapLieu()
        if tu == '0':
            return
    cayTuDien = xoaTu(cayTuDien, tu)
    os.system('cls')
    print("Từ điển sau khi xoá:")
    preOrderTraversal(cayTuDien)

    if tiepTuc() == 't':
        os.system('cls')
        loaiBoMotMucTu()

def traCuuCacNghiaCuaMotMucTu():
    global cayTuDien
    print("Nhập từ bạn muốn tra nghĩa, hoặc gõ số 0 để quay lại: ", end='')
    tu = kiemTraNhapLieu()
    if tu == '0':
        return
    nutTimThay = timTu(cayTuDien, tu)
    while nutTimThay is None:
        print("Từ bạn nhập không có trong từ điển vui lòng nhập lại, hoặc gõ số 0 để quay lại: ", end='')
        tu = kiemTraNhapLieu()
        if tu == '0':
            return
        nutTimThay = timTu(cayTuDien, tu)
    print(f"Các nghĩa của từ '{tu}' là:")
    for dinhNghia in nutTimThay.cacDinhNghia:
        print(f"Loại từ: {dinhNghia.loaiTu}")
        print(f"Nghĩa: {dinhNghia.nghia}")
        print(f"Ví dụ: {dinhNghia.viDu}")
    
    if tiepTuc() == 't':
        os.system('cls')
        traCuuCacNghiaCuaMotMucTu()

def luuTuDienVaoCacTapTin():
    global cayTuDien
    tenTapTin = "N21DCDT016_BST.txt"
    tapTin = open(tenTapTin, 'w')

    def preOrderTraversalWithFileSave(tuGoc, tapTin):
        if not tuGoc:
            return 
        chuoiGhi = tuGoc.tu + "\n"
        for dinhNghia in tuGoc.cacDinhNghia:
            chuoiGhi += dinhNghia.loaiTu + "\n" + dinhNghia.nghia + "\n" + dinhNghia.viDu + "\n"
        tapTin.write(chuoiGhi + "\n")
        preOrderTraversalWithFileSave(tuGoc.tuTrai, tapTin)
        preOrderTraversalWithFileSave(tuGoc.tuPhai, tapTin)

    preOrderTraversalWithFileSave(cayTuDien, tapTin)
    tapTin.close()
    print(f"Từ điển đã được lưu thành công vào tập tin {tenTapTin}")
    khongGiCa = input("Nhan enter de tiep tuc:")

def napTuDienTuCacTapTin():
    global cayTuDien
    tenTapTin = "N21DCDT016_BST.txt"
    tapTin = open(tenTapTin, 'r')

    for dong in tapTin:
        dong = dong.strip()
        if not dong:  
            continue

        tu = dong  
        loaiTu = tapTin.readline().strip()  
        nghia = tapTin.readline().strip() 
        viDu = tapTin.readline().strip() 

        dinhNghia = DinhNghia(loaiTu, nghia, viDu)
        nutMoi = AVLNode(tu)
        nutMoi.themCacDinhNghia(dinhNghia)
        cayTuDien = chenTu(cayTuDien, nutMoi)

    tapTin.close()
    print(f"Từ điển đã được nạp thành công từ tập tin {tenTapTin}")
    khongGiCa = input("Nhan enter de tiep tuc:")

cayTuDien = None
hienMenu()
 
