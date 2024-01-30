def xoaychieu(mang_a):
    chi_so_dau = 0
    chi_so_cuoi = len(mang_a) - 1

    while chi_so_dau < chi_so_cuoi:
        temp_1 = mang_a[chi_so_dau]
        mang_a[chi_so_dau] = mang_a[chi_so_cuoi]
        mang_a[chi_so_cuoi] = temp_1
        chi_so_dau += 1
        chi_so_cuoi -= 1
    print(mang_a)
        

mang_a = [1,2,3,4,5]

xoaychieu(mang_a)



