def nhietDoTrBVaSoNgayCaoHonTrB(so_ngay, nhiet_do):
    nhiet_do_trb = 0.0
    
    for i in nhiet_do:
        nhiet_do_trb += i
    
    nhiet_do_trb /= so_ngay
    print("Average =", nhiet_do_trb)

    dem = 0

    for i in nhiet_do:
        if i > nhiet_do_trb:
            dem += 1

    print(dem, "day(s) above averge")


from array import *
nhiet_do = array('i',[])

so_ngay = int(input("How many day's temperature? "))

for i in range(so_ngay):
    temp = int(input("Day "+str(i+1)+"s high temp: "))
    nhiet_do.append(temp)

nhietDoTrBVaSoNgayCaoHonTrB(so_ngay, nhiet_do)

