def Palindrome(mang_a):
    chi_so_dau = 0
    chi_so_cuoi = len(mang_a) - 1

    while chi_so_dau < chi_so_cuoi:
        if mang_a[chi_so_dau] != mang_a[chi_so_cuoi]:
            return False
        chi_so_dau += 1
        chi_so_cuoi -= 1
    return True
    


a = input("nhap mang cua ban: ")
a = a.split()  
mang_a = [int(x) for x in a]  


if(Palindrome(mang_a)):
    print("La mang palindrome")
else:
    print("khong la mang palindrome")