def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i
    
    for i in array:
        product *= i
    print("Sum = "+str(sum)+", Product = "+str(product))

def lay_mang():
    nhap_chuoi = input("nhap phan tu cua mang: ")
    chuyen_chuoi = nhap_chuoi.split()
    array = [int(x) for x in chuyen_chuoi]
    return array

mang_vua_nhap = lay_mang()

foo(mang_vua_nhap)
