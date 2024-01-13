def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print("dang mo con thu", doll)
        openRussianDoll(doll - 1)

so_bup_be = int(input("nhap so luong bup be: "))
openRussianDoll(so_bup_be)